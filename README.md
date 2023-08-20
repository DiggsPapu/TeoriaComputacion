# Laboratorio 4
Diego Andrés Alonzo Medinilla 20172
Samuel Argueta 211024
## Ejercicio 1
### Instrucciones
* En laboratorios anteriores implementó un balanceo de expresiones regulares, luego implementó Shunting Yard para convertir una Expresión Regular en notación infix a postfix y por último creó un árbol abstracto sintáctico que representa la expresión en postfix de forma visual. Ahora, utilizando todos estos elementos, deberá construir (con base en el árbol generado) el AFN resultante de aplicar el algoritmo de Thompson al árbol construido y mostrar su dibujo en pantalla, así como deberá también simular el AFN para reconocer cadenas de la expresión regular asociada. Especificación del funcionamiento del programa
* Entrada
    * Una expresión regular r.
    * Una cadena w.
* Salida
    * Por cada AFN generado a partir de r:
* Una imagen con el Grafo correspondiente para el AFN generado, mostrando el estado inicial, los estados adicionales, el estado de aceptación y las transiciones con sus símbolos correspondientes.
* La simulación del AFN al colocar la cadena w: el programa debe indicar si w ∈ L(r) con un "sí" en caso el enunciado anterior sea correcto, de lo contrario deberá mostrar un "no".
* Su programa debe leer un archivo de texto y procesar cada línea en este archivo. Cada
línea deberá de tener una expresión regular, correspondiente a la siguiente lista:
    * (𝑎 ∗ |𝑏 ∗) +
    * ((𝜀|𝑎)|𝑏 ∗) ∗
    * (𝑎|𝑏) ∗ 𝑎𝑏𝑏(𝑎|𝑏) ∗
    * 0? (1? )? 0 ∗
* Muestre la ejecución completa de su programa y explique brevemente en el video su código.
### Notas
* Primero que nada se debe de notar que se hizo un make para poder convertir los archivos .dot a png's de manera que puedan ser visibles. 
    * Se ejecuta make -f [direccion del archivo make] para generar los archivos png's.
    * Se ejecuta make -f [direccion del archivo make] clean para limpiar de los archivos png's.
### Resultados
* (𝑎 ∗ |𝑏 ∗) +
   * Arbol

     ![graph1](https://github.com/DiggsPapu/TeoriaComputacion/assets/84475020/160dd4d9-b685-446f-a1c2-e224bcc3f60b)
   * AFN

     ![afn1](https://github.com/DiggsPapu/TeoriaComputacion/assets/84475020/a28f227a-e174-4049-9079-3e2e182643f4)

* ((𝜀|𝑎)|𝑏 ∗) ∗
   * Arbol

     !![graph2](https://github.com/DiggsPapu/TeoriaComputacion/assets/84475020/397bd5f7-fead-4a07-a8b7-fc548aa0c0f5)
   * AFN

     ![afn2](https://github.com/DiggsPapu/TeoriaComputacion/assets/84475020/47254660-4261-4cb8-b9f8-c8b8440426c9)

* (𝑎|𝑏) ∗ 𝑎𝑏𝑏(𝑎|𝑏) ∗
   * Arbol

     ![graph3](https://github.com/DiggsPapu/TeoriaComputacion/assets/84475020/30276a87-a854-4e04-9a06-0204085a6cb0)
   * AFN

     ![afn3](https://github.com/DiggsPapu/TeoriaComputacion/assets/84475020/cc74b404-25e1-4b43-bd53-28d2aaa82e2e)

* 0? (1? )? 0 ∗
   * Arbol

     ![graph4](https://github.com/DiggsPapu/TeoriaComputacion/assets/84475020/3e5bf44d-21f3-46f3-b372-db90853c04df)
   * AFN

     ![afn4](https://github.com/DiggsPapu/TeoriaComputacion/assets/84475020/f22716b9-1351-44ba-8d62-bf3ad30b9181)


### Link al video
* https://youtu.be/i_AofrNu4DQ
## Ejercicio 2
### Instrucciones
* Utilice el Pumping Lemma para demostrar que el Lenguaje 𝐴 = {𝑦𝑦 | 𝑦 ∈ {0,1}∗ } no es regular.
* 𝑦 son todas las cadenas que pueden ser generadas con 0’s y 1’s.
* El lenguaje está conformado entonces por todas las cadenas 𝑦 seguidas de la misma 𝑦. Por ejemplo, si 𝑦 = 01 entonces una cadena parte del lenguaje será 𝑦𝑦 = 0101.
* Tome como base de su demostración que 𝑆 = 0" 10" 1, con P = pumping length.

