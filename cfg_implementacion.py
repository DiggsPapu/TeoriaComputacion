
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

  # Separar los no terminales, de las derivaciones, {no Terminal: derivacion]}
  gramatica_separada_1 = {}
  for gramaticas in gramatica:
    gramatica_separada_1[gramaticas[0]] = gramaticas[1].split(" ")

  # obtencion de las producciones con epsilon, se utiliza $ como epsilon
  anulables_1 = set()
  # Recorrer el diccionario de la gramatica en busca de epsilon ($)
  for clave_original, valor_original in gramatica_separada_1.items():
    # en caso de hallar un epsilon
    if '$' in valor_original:
      # almacenar el no terminal del cual proviene
      anulables_1.add(clave_original)

  # Encontrar las nuevas producciones
  nuevas_producciones_1 = []
  resultado_sin_epsilon = {}
  sin_copias_1 = []
    
  for clave_original_1, valor_original_1 in gramatica:
    terminal_original = []
    # Obtener las derivaciones que posee el no terminal
    if isinstance(valor_original_1, list):      
      terminal_original.extend(valor_original_1)
    else:
      terminal_original.append(valor_original_1)
    nuevo_cuerpo_1 = []
    #print(terminal_original)
    # leer cada una de las transiciones
    for derivacion_1_1 in terminal_original:
      # obtener los no terminales de la lista anulables
      #print(f"derivacion: {derivacion}")
      if "$" in derivacion_1_1:
        # Ignorar el valor epsilon ($)
        nuevo_cuerpo_1.append(derivacion_1_1.replace("$",""))
        continue
      else:
        # Recorrer los no terminales que poseen epsilon ($)
        for noTerminal in anulables_1:
          #print(f"no terminal: {noTerminal}, derivacaion:{derivacion}")
          # Verificar si el no terminal esta en la cadena derivable
          if noTerminal in derivacion_1_1:
            #print(f"Derivacion: {derivacion_1_1}")
            #print(f"no terminal: {noTerminal}, derivacaion:{derivacion_1_1}, verdad")
            # hacer la copia, pero con el caso donde el no terminal es epsilon
            nuevo_cuerpo_1.append(derivacion_1_1)
            nuevo_cuerpo_1.append(derivacion_1_1.replace(noTerminal,""))
      # agregar la nueva derivacion que se ha generado segun el simbolo
      nuevo_cuerpo_1.append(derivacion_1_1)
      # eliminar elementos repetidos
      sin_copias_1 = set(nuevo_cuerpo_1)
      nuevo_cuerpo_1 = list(sin_copias_1)
    # almacenar los valores segun sus claves, en este caso, segun el simbolo
    nuevas_producciones_1.append(nuevo_cuerpo_1)
    #print(f"nuevas producciones sin epsilon: {nuevas_producciones}")
    # volver un diccionario a su estado original 
    for i_1 in range (len(nuevas_producciones_1)):
      cadena_1 = "<--->".join(nuevas_producciones_1[i_1])
      resultado_sin_epsilon[clave_original_1] = cadena_1
    print(f"resultado final: {resultado_sin_epsilon}")
  return resultado_sin_epsilon

def eliminar_producciones_unitarias(gramatica_2):
  '''
    Funcion para eliminar las producciones unitarias de la gramatica.

    Args:
    gramatica_2 (dict): gramatica sin producciones epsilon para ser depurada
    de las producciones unitarias.

    Returns:
    resultado_sin_producciones_unitarias (dict): Gramatica depurada de las
    producciones unitarias 
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
        if len(producciones_2[i_2][j_2])  < 2 and producciones_2[i_2][j_2].isupper():
          #print(f"PRODUCCIONES A COMPARAR: {producciones_2[i_2][j_2].isupper()}")
          producciones_2[i_2][j_2] = gramatica_2[producciones_2[i_2][j_2]]
          producciones_unitarias_presentes = True
  #print(producciones)
  #print(f"PRODUCCIONES UNITARIAS DE LA GRAMATICA: {producciones_2}")
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
    Este metodo sirve para poder eliminar los elementos inutiles en la gramatica.

    Args:
    gramatica_3 (dict): Gramatica depurada sin producciones epsilon, ni producciones unitarias

    Returns:
    resultado_sin_inutiles (dict): Gramatica depurada sin los elementos inutiles.
  '''
  simbolos_3, producciones_3, nuevas_producciones_3 = [], [], []
  resultado_sin_inutiles = {}
  diccionario_detallado_3 = {} # este representa el diccionario original, pero con las producciones sin el | y en un arreglo
  # obtener los simbolos por aparte, asi como las producciones sin el |
  for clave_3, valor_3 in gramatica_3.items():
    #print(f"{clave_3} -> {valor_3}")
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

def forma_normal_chomsky(gramatica_4):
  '''
    Este metodo lleva a la gramatica a su etapa final, que es la forma
    normal de chomsky.

    Args:
    gramatica_4 (dict): Gramatica simplificada previament

    Returns:
    gramatica_4 (dict): Devuelve la gramatica en forma de chomsky
    gramatica_4_1 (dict): Devuelve la gramatica no forma de chomsky

  '''

  llaves_4, derivaciones_4 = [], []
  valores_terminales_4 = []

  gramatica_4_1 = {}
  # descomponer el diccionario de la gramatica, separando los simbolos de las derivaciones
  #print(gramatica_4)
  for llave_4, derivacion_4 in gramatica_4.items():
    llaves_4.append(llave_4)
    derivaciones_4.append(derivacion_4.split("|")) 
    gramatica_4_1[llave_4] = derivacion_4
  
  # observar cuales son los elementos derivados, es decir, diferentes de lo simbolos
  for i_4 in range (len(derivaciones_4)):# recorrer el arreglo de arreglos
    for elemento_4 in derivaciones_4[i_4]: # para cada cadena del arreglo actual
        if elemento_4.islower(): # verificar si la cadena esta en minusculas. Las mayusculas son NoTerm.
          valores_terminales_4.append(elemento_4.replace(" ",""))
        else:
            continue
  # terminales no repetidos.
  eliminar_valores_terminales_repetidos = set(valores_terminales_4)
  valores_terminales_4 = list(eliminar_valores_terminales_repetidos)
  
  # agregar los nuevos valores no terminales
  nuevos_noTerminales_4 = {}
  for i_40 in range(len(valores_terminales_4)):
    arreglo_4 = []
    arreglo_4.append(valores_terminales_4[i_40])
    gramatica_4["C"+str(i_40)] = arreglo_4
    nuevos_noTerminales_4[valores_terminales_4[i_40]] = "C"+str(i_40)

  for i_41 in range(len(derivaciones_4)):
    for j_41 in range(len(derivaciones_4[i_41])):
      if derivaciones_4[i_41][j_41] in valores_terminales_4:
          derivaciones_4[i_41][j_41] = nuevos_noTerminales_4[derivaciones_4[i_41][j_41]]

  for i_42 in range(len(llaves_4)):
    gramatica_4[llaves_4[i_42]] = derivaciones_4[i_42]

  return gramatica_4, gramatica_4_1
