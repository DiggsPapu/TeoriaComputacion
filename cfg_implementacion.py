
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
  gramatica_separada_1 = []
  for gramaticas in gramatica:
    gramatica_separada_1.append(gramaticas.split("->"))

  #print(gramatica_separada)

  # obtencion de las producciones con epsilon, se utiliza $ como epsilon
  anulables_1 = set()
  # Recorrer el arreglo de arreglos
  for produccion_1 in range (len(gramatica_separada_1)):
    # Recorrer los elementos de cada arreglo del arreglo de arreglos
    for derivacion_1 in gramatica_separada_1[produccion_1]:
      # Verificar si hay epsilon, [0]->No terminal, [1]-> Terminal/derivacion
      if '$' in gramatica_separada_1[produccion_1][1]:
        # En caso de contener epsilon, obtener el valor no terminal y almacenarlo
        anulables_1.add(gramatica_separada_1[produccion_1][0])
  #print(f"deteccion de elementos con epsilon: {anulables}")
  # ---------------------------------------------------
  # Encontrar las nuevas producciones
  
  nuevas_producciones_1 = []
  resultado_sin_epsilon = {}
  sin_copias_1 = []
    
  for produccion_1 in gramatica:
    # Dividir la cadena en "->"
    partes_1 = produccion_1.split("->")      
    #obtener el valor no terminal (lado izquierdo de la flecha)
    non_terminal = partes_1[0].strip()
    #print(f"simbolo: {non_terminal}")
    # Obtener las derivaciones que posee el no terminal, lado derecho de la flecha
    cuerpo_1 = partes_1[1].split("|")
    #print(f"cuerpo: {cuerpo}")
    nuevo_cuerpo_1 = []
    # leer cada una de las transiciones
    for derivacion_1_1 in cuerpo_1:
      # obtener los no terminales de la lista anulables
      #print(f"derivacion: {derivacion}")
      if "$" in derivacion_1_1:
        # Ignorar el valor epsilon ($)
        continue
      else:            
        # Recorrer los no terminales que poseen epsilon ($)
        for noTerminal in anulables_1:
          #print(f"no terminal: {noTerminal}, derivacaion:{derivacion}")
          # Verificar si el no terminal esta en la cadena derivable
          if noTerminal in derivacion_1_1:
            #print(f"Derivacion: {derivacion}")
            #print(f"no terminal: {noTerminal}, derivacaion:{derivacion}, verdad")
            # hacer la copia, pero con el caso donde el no terminal es epsilon
            cadena_modificada_1 = derivacion_1_1.replace(noTerminal,"")
            if cadena_modificada_1 != "":
              nuevo_cuerpo_1.append(derivacion_1_1)
              nuevo_cuerpo_1.append(cadena_modificada_1)
      # agregfar la nueva derivacion que se ha generado segun el simbolo
      nuevo_cuerpo_1.append(derivacion_1_1)
      # eliminar elementos repetidos
      sin_copias_1 = set(nuevo_cuerpo_1)
      nuevo_cuerpo_1 = list(sin_copias_1)
    # almacenar los valores segun sus claves, en este caso, segun el simbolo
    nuevas_producciones_1.append(nuevo_cuerpo_1)
    #print(f"nuevas producciones sin epsilon: {nuevas_producciones}")
    # volver un diccionario a su estado original 
    for i_1 in range (len(nuevas_producciones_1)):
      cadena_1 = "|".join(nuevas_producciones_1[i_1])
      resultado_sin_epsilon[non_terminal] = cadena_1
    #print(f"resultado final: {resultado_sin_epsilon}")
  return resultado_sin_epsilon

def eliminar_producciones_unitarias(gramatica_2):
  '''
  '''
  simbolos_2, producciones_2, nuevas_producciones_2 = [], [], []
  resultado_sin_producciones_unitarias = {}

  # Obtener los símbolos y producciones del diccionario
  for clave_2, valor_2 in gramatica_2.items():
    #print(f"{clave} -> {valor}")
    simbolos_2.append(clave_2)
    producciones_2.append(valor_2.split("|"))

  producciones_unitarias_presentes = True
  # obtener las producciones unitarrias de toda la gramatica
  while producciones_unitarias_presentes:
    producciones_unitarias_presentes = False
    # recorrer las producciones
    for i_2 in range (len(producciones_2)):
      for j_2 in range (len(producciones_2[i_2])):
            
        for simbolo_2 in simbolos_2:
          # Verificar si hay una produccion unitaria en la derivaciones, segun el simbolo
          # en este caso, si hay un simbolo, es decir, solo la letra S en una derivaciones
          # se toma como unitaria.
          if producciones_2[i_2][j_2] == simbolo_2:
            producciones_2[i_2][j_2] = gramatica_2[producciones_2[i_2][j_2]]
            producciones_unitarias_presentes = True
  #print(producciones)
  
  for i_22 in range (len(producciones_2)):
    cadena = "|".join(producciones_2[i_22])
    nuevas_producciones_2.append(cadena)
  #print(nuevas_producciones)
  for i_222 in range (len(nuevas_producciones_2)):
    resultado_sin_producciones_unitarias[simbolos_2[i_222]] = nuevas_producciones_2[i_222]
  #print(resultado)
  return resultado_sin_producciones_unitarias

def eliminar_simbolos_inutiles(gramatica_3):
  '''
  '''
  simbolos_3, producciones_3, nuevas_producciones_3 = [], [], []
  resultado_sin_inutiles = {}
  diccionario_detallado_3 = {} # este representa el diccionario original, pero con las producciones sin el | y en un arreglo
  # obtener los simbolos por aparte, asi como las producciones sin el |
  for clave_3, valor_3 in gramatica_3.items():
    print(f"{clave_3} -> {valor_3}")
    simbolos_3.append(clave_3)
    producciones_3.append(valor_3.split("|"))

  # diccionario para tener las validaciones separadas  
  for i_324 in range (len(simbolos_3)):
    diccionario_detallado_3[simbolos_3[i_324]] = producciones_3[i_324]
  #print(producciones)
  #print(simbolos)
  #print(diccionario_detallado)

  no_utiles = []
  # recorrer los arreglos de producciones
  for i_3 in range (len(producciones_3)):
    # recorrer las producciones de cada arreglo
    for j_3 in range (len(producciones_3[i_3])):
      # obtener los caracteres que componen la produccion
      arreglo_caracteres_3 = [caracter for caracter in producciones_3[i_3][j_3]]
      # recorrer los caracteres
      for k_3 in range (len(arreglo_caracteres_3)):
        # verificar si uno de esos caracteres en mayuscula no es un simbolo
        if arreglo_caracteres_3[k_3].isupper() and arreglo_caracteres_3[k_3] not in simbolos_3:
          cadena_3 = "".join(arreglo_caracteres_3)
          no_utiles.append(cadena_3)

  # eliminar los elementos repetidos
  conjunto_sin_duplicado_3 = set(no_utiles)
  no_utiles = list(conjunto_sin_duplicado_3)

  # eliminar los elementos que no llevan para nada.
  for clave_30, valor_30 in diccionario_detallado_3.items():
    for elemento_a_eliminar_30 in no_utiles:
      if elemento_a_eliminar_30 in valor_30:
        valor_30.remove(elemento_a_eliminar_30)
  
  # eliminar, en caso de haber un simbolo que no lleva a nada
  claves_eliminar_3 = []
  for clave_31, valor_31 in diccionario_detallado_3.items():
    if not valor_31:
     claves_eliminar_3.append(clave_31)

  for clave_32 in claves_eliminar_3:
    del diccionario_detallado_3[clave_32]
  #print(diccionario_detallado)

  # reiniciar los arreglos prvios con los nuevos valores
  simbolos_3.clear()
  producciones_3.clear()
  # ver si hay mas elementos que no ayudan en la gramatica
  for clave_33, valor_33 in diccionario_detallado_3.items():
    simbolos_3.append(clave_33)
    producciones_3.append(valor_33)

  # obtener los elemetos que si derivan desde el estado inicial
  elementos_validos = []
  for i_30 in range (len(producciones_3)):
    for j_30 in range (len(producciones_3[i_30])):
      for k_30 in range (len(simbolos_3)):
        if simbolos_3[k_30] in producciones_3[i_30][j_30]:
          elementos_validos.append(simbolos_3[k_30])
  # se toma por defecto el estado inicial
  elementos_validos.append("S")
  #print(elementos_validos)

  elementos_no_validos = []
  for i_31 in range (len(simbolos_3)):
    if simbolos_3[i_31] not in elementos_validos:
      elementos_no_validos.append(simbolos_3[i_31])
  #print(elementos_no_validos)
  
  # se termina de depurar
  for i_32 in range (len(elementos_no_validos)):
    del diccionario_detallado_3[elementos_no_validos[i_32]]
  #print(diccionario_detallado)

  simbolos_3.clear()
  producciones_3.clear()
  for clave_34, valor_34 in diccionario_detallado_3.items():
    simbolos_3.append(clave_34)
    producciones_3.append(valor_34)
  for i_33 in range (len(producciones_3)):
    cadena = "|".join(producciones_3[i_33])
    nuevas_producciones_3.append(cadena)

  for i_34 in range (len(nuevas_producciones_3)):
    resultado_sin_inutiles[simbolos_3[i_34]] = nuevas_producciones_3[i_34]
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
