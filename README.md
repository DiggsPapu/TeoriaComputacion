## Laboratorio 2
Diego Andrés Alonzo Medinilla 20172
Samuel Argueta 211024
# Ejercicio 1
- Convierta las siguientes expresiones regulares en autómatas finitos
deterministas (para ello deberá primero convertir las expresiones regulares a AFN y luego convertir
a AFD). Muestre todo su procedimiento, i.e., AFN construido con Thompson, tabla de transición,
conversión a AFD. Para el inciso g, interprete \ como un escape de carácter, i.e., \( significa que su
regex reconoce el caracter (.
  -(𝑎|𝑡)𝑐
  - (𝑎|𝑏) ∗
  - (𝑎 ∗ |𝑏 ∗) ∗
  - ((𝜀|𝑎)|𝑏 ∗) ∗
  - (𝑎|𝑏) ∗ 𝑎𝑏𝑏(𝑎|𝑏) ∗
  - 0? (1? )? 0 ∗
  - 𝑖𝑓\([𝑎𝑒] +\)\{[𝑒𝑖] +\}(\𝑛(𝑒𝑙𝑠𝑒\{[𝑗𝑙] +\}))?
  - [𝑎𝑒03] + @[𝑎𝑒03]+. (𝑐𝑜𝑚|𝑛𝑒𝑡|𝑜𝑟𝑔)(. (𝑔𝑡|𝑐𝑟|𝑐𝑜))?
- En la carpeta PDF se encuentra el documento donde se realizo la primera parte del laboratorio
# Ejercicio 2
- Escriba código en el lenguaje de programación de su gusto para
implementar un algoritmo capaz de balancear expresiones en formato infix. Implemente el uso de
una pila para llevar track de los símbolos de interés, i.e., (), [], {}, para definir el buen balanceo.
- Video del ejercicio: https://youtu.be/MI-A0jBjaPE
# Ejercicio 3
- Escriba código en el lenguaje de programación de su gusto para
implementar el algoritmo de Shunting Yard para convertir expresiones regulares en notación infix a
notación postfix.
- Contexto: El algoritmo de Shunting Yard consiste en un algoritmo desarrollado por Eric Dijkstra, este algoritmo permite analizar una expresión y convertirlo a un valor válido para su posterior manejo. Consiste en tener dos stacks de manera que uno de los stacks será para almacenar operadores, mientras que el otro stack servirá para almacenar símbolos.
- Explicación del algorimo:
  - Se inicia a recorrer la expresión.
  - En caso de que se encuentre con un operador se mete en el stack de operaciones.
    - Sí no está vacía se verifica que la precedencia de la punta del stack sea menor que la precedencia del token actual.
      - Se empiezan a sacar los operadores del stack hasta que esté vacío.
      - Se mete en el stack de operaciones.
    - Sí está vacía se mete en el stack de operaciones.
  - En caso de que se encuentre con un símbolo se mete en el stack de símbolos.
  - Cuando se termine de recorrer la cadena se saca todo lo que está en el stack de operaciones y se mete en el stack de símbolos.
- Video ejercicio: https://youtu.be/XxtqLINrSko
