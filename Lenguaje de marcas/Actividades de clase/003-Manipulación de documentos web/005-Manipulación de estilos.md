```
'''
CSS y JavaScript
2026 Fabiana Sotillo
Estilo Condicional, Funciones de Cálculo en CSS y Manipulación de estilos con JavaScript
'''
```

---
En este ejercicio se trabajan varios conceptos fundamentales del desarrollo web, combinando CSS y JavaScript para crear interfaces dinámicas e interactivas. Se aplican técnicas de estilo condicional, funciones de cálculo en CSS, uso de variables y manipulación de clases mediante JavaScript. El objetivo de esta práctica es comprender cómo se pueden modificar estilos de forma dinámica en función de la interacción del usuario y cómo se pueden reutilizar estilos mediante variables y funciones, mejorando así la flexibilidad y mantenibilidad del código.

El ejercicio se compone de varios archivos HTML que permiten practicar distintos mecanismos de control y manipulación de estilos.

#### 1. Estilo condicional según longitud de texto
En el archivo 004-estilo condicional.html se utiliza JavaScript para detectar la longitud del texto introducido en un campo ```<input>```. Cuando el usuario escribe, se comprueba la longitud del contenido y se cambia dinámicamente el estilo del fondo del campo mediante clases CSS.

Si la longitud es exactamente de 9 caracteres:
- Se elimina la clase rojo.
- Se añade la clase verde.
- Se muestra el texto “Correcto”.

En caso contrario:
- Se elimina la clase verde.
- Se añade la clase rojo.
- Se muestra el texto “Incorrecto”.

De este modo se implementa un sistema de validación visual en tiempo real.


#### 2. Función de cálculo en CSS
En el archivo 006-funcion de calculo en css.html se emplea la función calc() de CSS para definir el ancho de un elemento combinando porcentajes y unidades fijas. Esta función permite realizar operaciones matemáticas directamente en las hojas de estilo, lo que aporta una gran flexibilidad en diseños responsivos.

La anchura del ```<div>``` se define como:
```
width: calc(50% + 100px);
```
Esto permite que el elemento siempre mida un 50% del contenedor más 100 píxeles adicionales.


#### 3. Manipulación de estilos con JavaScript
En el archivo 001-estilo en javascript.html se selecciona un párrafo mediante JavaScript y se modifica directamente su estilo cambiando el color del texto. Además, se puede añadir un evento de clic para alternar entre rojo y verde dinámicamente.

Este enfoque permite modificar propiedades CSS desde JavaScript sin necesidad de clases.


#### 4. Quitar clase dinámicamente
En el archivo 003-quitar clase.html se demuestra cómo eliminar una clase CSS de un elemento HTML usando JavaScript. Se selecciona un párrafo que inicialmente tiene la clase rojo y se elimina dicha clase mediante classList.remove().

Este mecanismo es muy útil para gestionar estilos dinámicos basados en la interacción del usuario.


#### 5. Uso de variables en CSS
En el archivo 005-variables en css.html se utilizan variables CSS definidas en :root. Estas variables permiten centralizar valores como colores y reutilizarlos en múltiples elementos.

De este modo, cambiando una sola variable se puede modificar el estilo de todo el documento.


#### 6. Añadir clase dinámicamente
En el archivo 002-anadir clase.html se demuestra cómo añadir una clase a un elemento HTML mediante JavaScript usando classList.add(). Esto permite aplicar estilos de forma dinámica según eventos o condiciones.

---
#### Aplicación práctica

Estilo condicional por longitud:
```
<script>
let entrada = document.querySelector("input");
entrada.onkeyup = function(){
  let longitud = this.value.length;
  if(longitud == 9){
    this.classList.add("verde");
    this.classList.remove("rojo");
  }else{
    this.classList.remove("verde");
    this.classList.add("rojo");
  }
}
</script>
```

Función de cálculo en CSS:
```
div{
  width: calc(50% + 100px);
  background: red;
}
```

Modificación de estilo con JavaScript:
```
<script>
let parrafo = document.querySelector("p");
parrafo.style.color = "red";
</script>
```

Quitar clase:
```
<script>
let parrafo = document.querySelector("p");
parrafo.classList.remove("rojo");
</script>
```

Variables en CSS:
```
:root{
  --color_primario:#ff0000;
}
p{color:var(--color_primario);}
div{color:var(--color_primario);}
```

Añadir clase:
```
<script>
let parrafo = document.querySelector("p");
parrafo.classList.add("rojo");
</script>
```

---
Este ejercicio permite comprender cómo combinar CSS y JavaScript para crear interfaces dinámicas y adaptativas. A través del uso de estilos condicionales, funciones de cálculo, variables CSS y manipulación de clases, se refuerza el concepto de separación entre estructura, estilo y comportamiento. 

Estas técnicas son esenciales para desarrollar aplicaciones web, ya que permiten validar datos en tiempo real, reutilizar estilos de forma eficiente y modificar la apariencia de los elementos según la interacción del usuario, mejorando la experiencia y la usabilidad de los sitios web.
