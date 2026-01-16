En este ejercicio se desarrolla un programa en Java que simula el funcionamiento básico de una cafetería, permitiendo crear distintos tipos de café y añadir ingredientes adicionales. A través de la definición de una clase llamada Café, se aplican los conceptos fundamentales de la programación orientada a objetos, como la creación de clases, atributos privados, constructores y métodos públicos. El objetivo principal es comprender cómo se modelan objetos del mundo real en un programa informático y cómo se gestionan sus propiedades y comportamientos mediante métodos.

El programa se basa en la definición de una clase denominada Café, que representa un producto de la cafetería. Esta clase contiene dos atributos privados: uno para almacenar el tipo de café y otro para guardar la lista de ingredientes adicionales.

Para inicializar los datos del objeto, se implementa un constructor que recibe como parámetros el tipo de café y una lista de ingredientes. Además, se crean dos métodos públicos: uno para agregar nuevos ingredientes y otro para mostrar por pantalla la información completa del café.

De esta forma, se respeta el principio de encapsulación, ya que los atributos solo pueden modificarse a través de métodos públicos, garantizando un acceso controlado a los datos del objeto.

---
A continuación se muestra el código funcional completo:
```
import java.util.ArrayList;

public class Cafe {

    // Atributos privados
    private String tipo;
    private ArrayList<String> ingredientes;

    // Constructor
    public Cafe(String tipo, ArrayList<String> ingredientes) {
        this.tipo = tipo;
        this.ingredientes = ingredientes;
    }

    // Método para agregar un ingrediente
    public void agregarIngrediente(String ingrediente) {
        ingredientes.add(ingrediente);
    }

    // Método para mostrar la información del café
    public void mostrarCafe() {
        System.out.println("Tipo de café: " + tipo);
        System.out.println("Ingredientes adicionales:");
        
        if (ingredientes.size() == 0) {
            System.out.println("No hay ingredientes adicionales.");
        } else {
            for (String ingrediente : ingredientes) {
                System.out.println("- " + ingrediente);
            }
        }
    }

    // Método main
    public static void main(String[] args) {

        // Crear un café tipo Latte sin ingredientes adicionales
        ArrayList<String> ingredientes = new ArrayList<>();
        Cafe miCafe = new Cafe("Latte", ingredientes);

        // Agregar ingredientes
        miCafe.agregarIngrediente("Leche descremada");
        miCafe.agregarIngrediente("Azúcar");

        // Mostrar el café creado
        miCafe.mostrarCafe();
    }
}
```

---
Al ejecutar el programa, se crea un objeto de la clase Café con el tipo "Latte". Posteriormente se añaden ingredientes adicionales mediante el método agregarIngrediente y finalmente se muestra toda la información del café utilizando el método mostrarCafe. El resultado por pantalla es una descripción completa del café creado.

Este ejercicio permite aplicar de forma práctica los conceptos de clases, objetos, atributos, constructores y métodos en Java. La simulación de una cafetería facilita la comprensión de cómo se pueden representar elementos del mundo real mediante programación orientada a objetos. Además, refuerza la importancia de la encapsulación y del uso de métodos públicos para gestionar la información interna de una clase, sentando las bases para el desarrollo de aplicaciones más complejas en futuras unidades.
