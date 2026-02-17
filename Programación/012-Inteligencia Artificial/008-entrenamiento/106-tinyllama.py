#!/usr/bin/env python3
import os
import torch
from datetime import datetime

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model


# ------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------
DATA_FILE = "004-preentrenamiento relleno.jsonl"
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
OUTPUT_DIR = "./tinyllama-1.1b-lora"

MAX_LENGTH = 256
NUM_EPOCHS = 1
LR = 2e-4
BATCH_SIZE = 1
GRAD_ACCUM = 4


def main():
    start_dt = datetime.now()

    print("🚀 Starting TinyLlama training (Q/A JSONL)")
    print(f"📄 Dataset: {DATA_FILE}")
    print(f"🧠 Base model: {MODEL_NAME}")
    print("-" * 60)

    if not os.path.isfile(DATA_FILE):
        raise FileNotFoundError(f"Training file not found: {DATA_FILE}")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cuda":
        print("💻 CUDA GPU detected. Training in fp16 with LoRA.")
    else:
        print("💻 No CUDA GPU. Training on CPU (this will be slower).")

    # ------------------------------------------------------------
    # Load dataset
    # ------------------------------------------------------------
    print("📥 Loading dataset...")
    raw_dataset = load_dataset(
        "json",
        data_files=DATA_FILE,
        split="train",
    )
    print(f"✅ Dataset loaded with {len(raw_dataset)} Q/A examples.")

    # ------------------------------------------------------------
    # Tokenizer and model
    # ------------------------------------------------------------
    print("✅ Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        use_fast=True,
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("✅ Loading base model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        device_map="auto" if device == "cuda" else None,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    )

    if device == "cpu":
        model.to(device)

    # ------------------------------------------------------------
    # LoRA
    # ------------------------------------------------------------
    print("✅ Wrapping model with LoRA...")
    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "gate_proj",
            "up_proj",
            "down_proj",
        ],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # ------------------------------------------------------------
    # Convert Q/A → chat text
    # ------------------------------------------------------------
    SYSTEM_PROMPT = (
        "Eres un asistente educativo en español que responde de forma clara, "
        "precisa y concisa a preguntas técnicas."
    )

    def qa_to_text(example):
        q = str(example.get("question", ""))
        a = str(example.get("answer", ""))

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": q},
            {"role": "assistant", "content": a},
        ]

        if hasattr(tokenizer, "apply_chat_template"):
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False,
            )
        else:
            text = (
                f"<|system|>\n{SYSTEM_PROMPT}\n"
                f"<|user|>\n{q}\n"
                f"<|assistant|>\n{a}\n"
            )

        return {"text": text}

    text_dataset = raw_dataset.map(qa_to_text)

    # ------------------------------------------------------------
    # Tokenization
    # ------------------------------------------------------------
    print("✅ Tokenizing dataset...")

    def tokenize_fn(batch):
        out = tokenizer(
            batch["text"],
            truncation=True,
            max_length=MAX_LENGTH,
            padding="max_length",
        )
        out["labels"] = out["input_ids"].copy()
        return out

    tokenized_dataset = text_dataset.map(
        tokenize_fn,
        batched=True,
        remove_columns=text_dataset.column_names,
    )

    # ------------------------------------------------------------
    # TrainingArguments
    # ------------------------------------------------------------
    print("✅ Configuring TrainingArguments...")

    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LR,
        weight_decay=0.01,
        warmup_ratio=0.03,
        logging_steps=10,
        save_steps=200,
        save_total_limit=1,
        fp16=(device == "cuda"),
        bf16=False,
        dataloader_pin_memory=False,
        report_to="none",
    )

    # ------------------------------------------------------------
    # Trainer
    # ------------------------------------------------------------
    print("✅ Creating Trainer...")
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    # ------------------------------------------------------------
    # Train
    # ------------------------------------------------------------
    print("🚂 Starting training...")
    train_output = trainer.train()
    print("🏁 Training finished.")

    # ------------------------------------------------------------
    # Save
    # ------------------------------------------------------------
    print("💾 Saving model and tokenizer to", OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("✅ Done.")

    end_dt = datetime.now()
    print(f"⏱️ Duration: {end_dt - start_dt}")
    metrics = getattr(train_output, "metrics", None)
    if metrics:
        print("📊 Metrics:", metrics)


if __name__ == "__main__":
    main()

