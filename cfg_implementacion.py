
# Función para eliminar producciones epsilon
def eliminar_producciones_epsilon(gramatica):
  '''
    Elimina producciones epsilon de una gramática.

    Esta función toma una gramática como entrada y elimina las producciones epsilon
    (producciones que generan una cadena vacía) de la gramática.

    Args:
        gramatica (list): Una lista de producciones de la gramática, donde cada
                          producción es una lista con dos elementos: el símbolo
                          no terminal y el cuerpo de la producción.

    Returns:
        dict: Un diccionario de producciones de la gramática modificada sin las
              producciones epsilon.

    Examples:
        >>> gramatica = [['S', 'AB|A|B|'], ['A', 'a'], ['B', 'b']]
        >>> eliminar_producciones_epsilon(gramatica)
        [['S', 'AB|A|B'], ['A', 'a'], ['B', 'b']]
  '''
  # Encontrar símbolos anulables

  # Separar los no terminales, de las derivaciones, [no Terminal, derivacion]
  gramatica_separada = []
  for gramaticas in gramatica:
    gramatica_separada.append(gramaticas.split("->"))

  #print(gramatica_separada)

  # obtencion de las producciones con epsilon, se utiliza $ como epsilon
  anulables = set()
  # Recorrer el arreglo de arreglos
  for produccion in range (len(gramatica_separada)) :   
    # Recorrer los elementos de cada arreglo del arreglo de arreglos
    for derivacion in gramatica_separada[produccion]:
      # Verificar si hay epsilon, [0]->No terminal, [1]-> Terminal/derivacion
      if '$' in gramatica_separada[produccion][1]:
        # En caso de contener epsilon, obtener el valor no terminal y almacenarlo
        anulables.add(gramatica_separada[produccion][0])
  #print(f"deteccion de elementos con epsilon: {anulables}")
  # ---------------------------------------------------
  # Encontrar las nuevas producciones
  
  nuevas_producciones = []
  resultado_sin_epsilon = {}
  sin_copias = []
    
  for produccion in gramatica:
    # Dividir la cadena en "->"
    partes = produccion.split("->")      
    #obtener el valor no terminal (lado izquierdo de la flecha)
    non_terminal = partes[0].strip()
    #print(f"simbolo: {non_terminal}")
    # Obtener las derivaciones que posee el no terminal, lado derecho de la flecha
    cuerpo = partes[1].split("|")
    #print(f"cuerpo: {cuerpo}")
    nuevo_cuerpo = []
    # leer cada una de las transiciones
    for derivacion in cuerpo:
      # obtener los no terminales de la lista anulables
      #print(f"derivacion: {derivacion}")
      if "$" in derivacion:
        # Ignorar el valor epsilon ($)
        continue
      else:            
        # depurar los epsilon
        for noTerminal in anulables:
          # Verificar si el no terminal esta en la cadena derivable
          if noTerminal in derivacion:
            # hacer la copia, pero con el caso donde el no terminal es epsilon
            cadena_modificada = derivacion.replace(noTerminal,"")
            print(f"cadena modificada: {cadena_modificada}")
            if cadena_modificada != "":
              nuevo_cuerpo.append(derivacion)
              nuevo_cuerpo.append(cadena_modificada)
      # agregfar la nueva derivacion que se ha generado segun el simbolo
      nuevo_cuerpo.append(derivacion)
      # eliminar elementos repetidos
      sin_copias = set(nuevo_cuerpo)
      nuevo_cuerpo = list(sin_copias)
    # almacenar los valores segun sus claves, en este caso, segun el simbolo
    nuevas_producciones.append(nuevo_cuerpo)
    #print(f"nuevas producciones sin epsilon: {nuevas_producciones}")
    # volver un diccionario a su estado original 
    for i in range (len(nuevas_producciones)):
      cadena = "|".join(nuevas_producciones[i])
      resultado_sin_epsilon[non_terminal] = cadena
    #print(f"resultado final: {resultado_sin_epsilon}")
  return resultado_sin_epsilon

def eliminar_producciones_unitarias(gramatica):
  '''
  '''
  simbolos, producciones, nuevas_producciones = [], [], []
  resultado = {}

  # Obtener los símbolos y producciones del diccionario
  for clave, valor in gramatica.items():
    #print(f"{clave} -> {valor}")
    simbolos.append(clave)
    producciones.append(valor.split("|"))

  #print(f"simbolos: {simbolos}, producciones: {producciones}")
  
  producciones_unitarias_presentes = True
  # obtener las producciones unitarrias de toda la gramatica
  while producciones_unitarias_presentes:
    producciones_unitarias_presentes = False
    # recorrer las producciones
    for i in range (len(producciones)):
      for j in range (len(producciones[i])):
        for simbolo in simbolos:
          # Verificar si hay una produccion unitaria en la derivaciones, segun el simbolo
          # en este caso, si hay un simbolo, es decir, solo la letra S en una derivaciones
          # se toma como unitaria.
          if producciones[i][j] == simbolo:
            producciones[i][j] = gramatica[producciones[i][j]]
            producciones_unitarias_presentes = True
  #print(producciones)
  
  for i in range (len(producciones)):
    cadena = "|".join(producciones[i])
    nuevas_producciones.append(cadena)
  #print(nuevas_producciones)
  for i in range (len(nuevas_producciones)):
    resultado[simbolos[i]] = nuevas_producciones[i]
  #print(resultado)
  return resultado

def eliminar_simbolos_inutiles(gramatica):
  '''
  '''
  simbolos, producciones, nuevas_producciones = [], [], []
  resultado_sin_inutiles = {}
  diccionario_detallado = {} # este representa el diccionario original, pero con las producciones sin el | y en un arreglo
  # obtener los simbolos por aparte, asi como las producciones sin el |
  for clave, valor in gramatica.items():
    print(f"{clave} -> {valor}")
    simbolos.append(clave)
    producciones.append(valor.split("|"))

  # diccionario para tener las validaciones separadas  
  for i in range (len(simbolos)):
    diccionario_detallado[simbolos[i]] = producciones[i]
  #print(producciones)
  #print(simbolos)
  #print(diccionario_detallado)

  no_utiles = []
  # recorrer los arreglos de producciones
  for i in range (len(producciones)):
    # recorrer las producciones de cada arreglo
    for j in range (len(producciones[i])):
      # obtener los caracteres que componen la produccion
      arreglo_caracteres = [caracter for caracter in producciones[i][j]]
      # recorrer los caracteres
      for k in range (len(arreglo_caracteres)):
        # verificar si uno de esos caracteres en mayuscula no es un simbolo
        if arreglo_caracteres[k].isupper() and arreglo_caracteres[k] not in simbolos:
          cadena = "".join(arreglo_caracteres)
          no_utiles.append(cadena)

  # eliminar los elementos repetidos
  conjunto_sin_duplicado = set(no_utiles)
  no_utiles = list(conjunto_sin_duplicado)

  # eliminar los elementos que no llevan para nada.
  for clave, valor in diccionario_detallado.items():
    for elemento_a_eliminar in no_utiles:
      if elemento_a_eliminar in valor:
        valor.remove(elemento_a_eliminar)
  
  # eliminar, en caso de haber un simbolo que no lleva a nada
  claves_eliminar = []
  for clave, valor in diccionario_detallado.items():
    if not valor:
     claves_eliminar.append(clave)

  for clave in claves_eliminar:
    del diccionario_detallado[clave]
  #print(diccionario_detallado)

  # reiniciar los arreglos prvios con los nuevos valores
  simbolos.clear()
  producciones.clear()
  # ver si hay mas elementos que no ayudan en la gramatica
  for clave, valor in diccionario_detallado.items():
    simbolos.append(clave)
    producciones.append(valor)

  # obtener los elemetos que si derivan desde el estado inicial
  elementos_validos = []
  for i in range (len(producciones)):
    for j in range (len(producciones[i])):
      for k in range (len(simbolos)):
        if simbolos[k] in producciones[i][j]:
          elementos_validos.append(simbolos[k])
  # se toma por defecto el estado inicial
  elementos_validos.append("S")
  #print(elementos_validos)

  elementos_no_validos = []
  for i in range (len(simbolos)):
    if simbolos[i] not in elementos_validos:
      elementos_no_validos.append(simbolos[i])
  #print(elementos_no_validos)
  
  # se termina de depurar
  for i in range (len(elementos_no_validos)):
    del diccionario_detallado[elementos_no_validos[i]]
  #print(diccionario_detallado)

  simbolos.clear()
  producciones.clear()
  for clave, valor in diccionario_detallado.items():
    simbolos.append(clave)
    producciones.append(valor)
  for i in range (len(producciones)):
    cadena = "|".join(producciones[i])
    nuevas_producciones.append(cadena)

  for i in range (len(nuevas_producciones)):
    resultado_sin_inutiles[simbolos[i]] = nuevas_producciones[i]
  #print(resultado_sin_inutiles)
  return resultado_sin_inutiles


def forma_normal_chomsky(gramatica):
  '''
  '''
  llaves, derivaciones = [], []
  generador_de_sentencias = {}
  valores_terminales, listas_caracteres = [], []
  # descomponer el diccionario de la gramatica, separando los simbolos de las derivaciones
  for llave, derivacion in gramatica.items():
    llaves.append(llave)
    derivaciones.append(derivacion.split("|")) 

  # observar cuales son los elementos derivados, es decir, diferentes de lo simbolos
  for i in range (len(derivaciones)):# recorrer el arreglo de arreglos
    for elemento in derivaciones[i]: # para cada cadena del arreglo actual
      for caracter in elemento: # reocrrer la cadena
        if caracter.isupper(): # verificar si hay simbolos en el caracter
          continue
        else:
          valores_terminales.append(caracter) #de no haber, extraer el valor terminal

  eliminar_valores_terminales_repetidos = set(valores_terminales)
  valores_terminales = list(eliminar_valores_terminales_repetidos)
  #extraer los elementos que poseen mas de 2 caracteres
  sentencias_con_3_caracteres = []
  for i in range (len(derivaciones)):
    for j in range (len(derivaciones[i])):
      if len(derivaciones[i][j]) >= 3:
        sentencias_con_3_caracteres.append(derivaciones[i][j])
  # eliminar elementos repetidos, en caso de haber
  sentencias_sin_repeticion = set(sentencias_con_3_caracteres)
  sentencias_con_3_caracteres = list(sentencias_sin_repeticion)

   # este bloque funciona para poder reemplazar los valores con mas de 2 caracteres
  persistente = ""
  sobrante = ""
  simbolos_nuevos = []
  # Recorrer cada una de las cadenas
  for i in range (len(sentencias_con_3_caracteres)):
    # Recorrer cada carecter de la cadena
    for j in range (len(sentencias_con_3_caracteres[i])):
      # 
      if j == 1 and len(sentencias_con_3_caracteres[i]) >= 3:
        persistente = sentencias_con_3_caracteres[i][:j]
        sobrante = sentencias_con_3_caracteres[i][j:]
        detalles_modificacion = []
        if len(sobrante) < 3: # modificarlo, en caso de no haber cumplido la condicion y continuar teniendo mas
          simbolo = "C"+str(i)
          # almacenar el nuevo simbolo, lo que se va a cambiar, un registro del estado previo de la cadena
          # y la concatenacion del nuevo valor, a modo de quedar como chomsky
          detalles_modificacion.append(simbolo)
          detalles_modificacion.append(sobrante)
          detalles_modificacion.append(sentencias_con_3_caracteres[i])
          # concatenar los elementos que no se quitaron con el nuevo simbolo
          detalles_modificacion.append(persistente+simbolo)
          simbolos_nuevos.append(detalles_modificacion)
    # Repetir el ciclo, en caso de no tener un largo de 2
    if len(persistente) >= 3:
      sentencias_con_3_caracteres.append(persistente)
  #print(simbolos_nuevos)
  
  nuevos_simbolos_terminales = {}
  for i in range(len(valores_terminales)):
    gramatica["C"+str(i)+str(i)] = valores_terminales[i]
    nuevos_simbolos_terminales["C"+str(i)+str(i)] = valores_terminales[i]
  print(f"observando gramatica: {gramatica}")
  print(f"observando los nuevos valores terminales: {nuevos_simbolos_terminales}")
  # Recorrer las actualizaciones segun chomsky
  for i in range (len(simbolos_nuevos)):
    # recorrer las derivcaionces originales
    for j in range (len(derivaciones)):
      # Recorrer cada una de las cadenas
      for n in range (len(derivaciones[j])):
        # en caso de tener similitud con la modificacion de chomsky
        if simbolos_nuevos[i][2] == derivaciones[j][n]:
          # actualizar el valor de la derivacion al nuevo
          derivaciones[j][n] = simbolos_nuevos[i][3]
  print(f"observando las modificaciones a las derivacionces originales: {derivaciones}")
  # Unir las cadenadas respectivas para volver a su estado original
  derivaciones_con_union = []

  for i in range (len(derivaciones)):
    derivacionces_segun_simbolos = []
    for j in range (len(derivaciones[i])):
      derivacionces_segun_simbolos.append("|".join(derivaciones[i]))
    derivaciones_con_union.append(derivacionces_segun_simbolos)
  
  # Arreglar para la gramatica 1, pues elimina un valor que no debe
  for i in range (len(derivaciones_con_union)):
    limpieza_repetido = set(derivaciones_con_union[i])
    derivaciones_con_union[i] = list(limpieza_repetido)
  
  for i in range (len(llaves)):
    for j in range (len(derivacionces_segun_simbolos)):
      for k in range (len(derivaciones_con_union[i])):
        gramatica[llaves[i]] = derivaciones_con_union[i][k]
  #print(gramatica)
  for i in range (len(simbolos_nuevos)):
    for j in range (len(simbolos_nuevos[i])):
      gramatica[simbolos_nuevos[i][0]] = simbolos_nuevos[i][1]
  
  return gramatica
