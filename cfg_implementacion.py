import re
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
    gramatica_separada_1[gramaticas[0]] = gramaticas[1].split(" | ")
  #print(f"Gramatica separada: {gramatica_separada_1}")
  # obtencion de las producciones con epsilon, se utiliza $ como epsilon
  anulables_1 = set()
  # Recorrer el diccionario de la gramatica en busca de epsilon ($)
  for clave_original, valor_original in gramatica_separada_1.items():
    # en caso de hallar un epsilon
    if 'e' in valor_original:
      # almacenar el no terminal del cual proviene
      anulables_1.add(clave_original)

  # Encontrar las nuevas producciones
  nuevas_producciones_1 = []
  resultado_sin_epsilon = {}
  sin_copias_1 = []
  #print(f"gramatica original: {gramatica}")
  for clave_original_1, valor_original_1 in gramatica:
    terminal_original = []
    # Obtener las derivaciones que posee el no terminal
    if isinstance(valor_original_1, list):      
      terminal_original.extend(valor_original_1.split("|"))
    else:
      terminal_original.append(valor_original_1)
    nuevo_cuerpo_1 = []
    #print(f"terminal original: {terminal_original}")
    # leer cada una de las transiciones
    for derivacion_1_1 in terminal_original:
      # obtener los no terminales de la lista anulables
      #print(f"derivacion: {derivacion_1_1}")
      # Recorrer los no terminales que poseen epsilon ($)
      for noTerminal in anulables_1:
        #print(f"no terminal: {noTerminal}, derivacaion:{derivacion_1_1}")
        # Verificar si el no terminal esta en la cadena derivable
        if noTerminal in derivacion_1_1:
          #print(f"Derivacion: {derivacion_1_1}")
          #print(f"no terminal: {noTerminal}, derivacaion:{derivacion_1_1}, verdad")
          # hacer la copia, pero con el caso donde el no terminal es epsilon
          nuevo_cuerpo_1.append(derivacion_1_1)
          nuevo_cuerpo_1.append(derivacion_1_1.replace(noTerminal,""))

      # agregar la nueva derivacion que se ha generado segun el simbolo
      nuevo_cuerpo_1.append(derivacion_1_1)
      for modificacion in range (len(nuevo_cuerpo_1)):
        # Eliminando las producciones epsilon
        nuevo_cuerpo_1[modificacion] = nuevo_cuerpo_1[modificacion].replace("e","")
        # eliminando espacios extra
        nuevo_cuerpo_1[modificacion] = nuevo_cuerpo_1[modificacion].replace("  "," ")
        # eliminando | que estan de mas y no sirve como concatenacion
        #nuevo_cuerpo_1[modificacion] = nuevo_cuerpo_1[modificacion].replace(" | ","")
      
      #print(f"Nuevo Cuerpo sin epsion: {nuevo_cuerpo_1}")
      # eliminar elementos repetidos
      sin_copias_1 = set(nuevo_cuerpo_1)
      nuevo_cuerpo_1 = list(sin_copias_1)
    # almacenar los valores segun sus claves, en este caso, segun el simbolo
    nuevas_producciones_1.append(nuevo_cuerpo_1)
    #print(f"nuevas producciones sin epsilon: {nuevas_producciones_1}")
    # volver un diccionario a su estado original 

    for i_1 in range (len(nuevas_producciones_1)):
      cadena_1 = "|".join(nuevas_producciones_1[i_1])
      resultado_sin_epsilon[clave_original_1] = cadena_1
  #print(f"resultado final: {resultado_sin_epsilon}")
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
  parejas = []
  # Obtener los símbolos y producciones del diccionario
  for clave_2, valor_2 in gramatica_2.items():
    temporal = []
    temporal.append(clave_2)
    temporal.append(clave_2)
    simbolos_2.append(clave_2)
    producciones_2.append(valor_2.split("|"))
    parejas.append(temporal)
  
    # Arreglando posible error en la gramatica
  for i_02 in range (len(producciones_2)):
    for j_02 in range (len(producciones_2[i_02])):
      if len(producciones_2[i_02][j_02]) == 2:
        # eliminar espacio en blanco de la gramatica
        try:
          producciones_2[i_02][j_02] = producciones_2[i_02][j_02].replace(" ","")
        except:
          pass
  # Reajustando gramatica con la modificacion
  for i_020 in range (len(simbolos_2)):
    gramatica_2[simbolos_2[i_020]] = "|".join(producciones_2[i_020])
  # Eliminando los espacios en blanco que estan de mas en la gramatica
  producciones_2 = [[elemento.strip() for elemento in sublista if elemento.strip()] for sublista in producciones_2]
  #print(f"Observando las producciones: {producciones_2}")
  #print(f"Observando la gramatica: {gramatica_2}")
  producciones_unitarias_presentes = True
  # obtener las producciones unitarrias de toda la gramatica
    # recorrer las producciones
  while producciones_unitarias_presentes:
    producciones_unitarias_presentes = False
    for i_2 in range (len(producciones_2)):
      for j_2 in range (len(producciones_2[i_2])):
        for simbolo_2 in simbolos_2:
          # Verificar si hay una produccion unitaria en la derivaciones, segun el simbolo
          # en este caso, si hay un simbolo, es decir, solo la letra S en una derivaciones
          # se toma como unitaria.
          if producciones_2[i_2][j_2] == simbolo_2:
            lista_temporal = gramatica_2[producciones_2[i_2][j_2]].split("|")
            for i_222 in range (len(lista_temporal)):
              producciones_2[i_2].append(lista_temporal[i_222])
            producciones_2[i_2].remove(simbolo_2)
            producciones_unitarias_presentes = True
                
  
  #print(f"Observando producciones modificadas: {producciones_2}")
  #print(producciones_unitarias_presentes)
  #print(f"PRODUCCIONES UNITARIAS DE LA GRAMATICA: {producciones_2}")
  for i_22 in range (len(producciones_2)):
    cadena = "|".join(producciones_2[i_22])
    nuevas_producciones_2.append(cadena)
  #print(nuevas_producciones)
  for i_222 in range (len(nuevas_producciones_2)):
    resultado_sin_producciones_unitarias[simbolos_2[i_222]] = nuevas_producciones_2[i_222]
  #print(resultado_sin_producciones_unitarias)
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

  # descomponer el diccionario de la gramatica, separando los simbolos de las derivaciones
  #print(gramatica_4)
  for llave_4, derivacion_4 in gramatica_4.items():
    llaves_4.append(llave_4)
    derivaciones_4.append(derivacion_4.split("|")) 
  #print(derivaciones_4)

  seleccion_regex = opciones()
  patron_a_utilizar = ""
  elementos_encontrados_por_regex = []
  if seleccion_regex == 1:
    patron_a_utilizar = r'[^a-zA-Z]'
  elif seleccion_regex == 2:      
    patron_a_utilizar = r'\b[a-z]+\b'
  
  
  # Encontrar los terminales que son diferentes de las letras mayusculas, pues estas representa no terminales
  for i_4 in range (len(derivaciones_4)):
    for elemento_4 in derivaciones_4[i_4]:
      # hallar los todos y hacerlos un arreglo
      elementos_encontrados = re.findall(patron_a_utilizar, elemento_4)
      elementos_encontrados_por_regex.extend(elementos_encontrados)

  # Eliminar los elementos repetidos    
  conjunto_sin_duplicado_4 = set(elementos_encontrados_por_regex)
  elementos_encontrados_por_regex = list(conjunto_sin_duplicado_4)
  # eleiminar los espacioes en blanco, en caso de haber
  elementos_encontrados_por_regex = [elemento for elemento in elementos_encontrados_por_regex if elemento != ' ']
  
  #print(elementos_encontrados_por_regex)
  # agregar los nuevos valores no terminales
  nuevos_noTerminales_4 = {}

  # agregar y crear diccionario. Esto sirve para luego hacer el reemplazo en el dict original  
  # Lista de letras disponibles
  letras_disponibles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  # Crear un diccionario de mapeo de letras
  mapeo_letras_4 = {}

  for i_40 in range(len(elementos_encontrados_por_regex)):
      simbolo = elementos_encontrados_por_regex[i_40]
      if simbolo not in mapeo_letras_4:
          # Si el símbolo aún no tiene una letra asignada, toma una de la lista
          letra_asignada = letras_disponibles.pop(0)
          
          if not letras_disponibles:
              # Si se agotaron las letras, comienza a generar combinaciones de letras
              nueva_letra = 'A'
              while nueva_letra in mapeo_letras_4.values():
                  nueva_letra = chr(ord(nueva_letra) + 1)
              letra_asignada += nueva_letra
              
          mapeo_letras_4[simbolo] = letra_asignada
      else:
          # Si el símbolo ya tiene una letra asignada, úsala
          letra_asignada = mapeo_letras_4[simbolo]

      # Asigna la letra en lugar de "Cn" como nombre para los nuevos símbolos
      nuevos_noTerminales_4[simbolo] = letra_asignada
      gramatica_4[letra_asignada] = simbolo
  # ----------------------------------------------------------------
  #print(nuevos_noTerminales_4)
  #print(gramatica_4)
  # reemplazar los elementos en las derivaciones que corresponda. Por ejemplo * con C1.
  for i_41 in range(len(derivaciones_4)):
    for j_41 in range(len(derivaciones_4[i_41])):
      #print(derivaciones_4[i_41][j_41])
      cadena_modificada = ""
      for elemento_gramatica in derivaciones_4[i_41][j_41]:
        if elemento_gramatica in elementos_encontrados_por_regex:
          elemento_gramatica = nuevos_noTerminales_4[elemento_gramatica]
        cadena_modificada += elemento_gramatica
      derivaciones_4[i_41][j_41] = cadena_modificada
  

  continuar_cortando = True
  partes_cortadas = {}
  while continuar_cortando:
    continuar_cortando = False
    for i_42 in range (len(derivaciones_4)):
      for j_42 in range (len(derivaciones_4[i_42])):
        # Eliminar los epscioas vacios, por ejemplo D E B -> DEB
        derivacion_sin_espacios = derivaciones_4[i_42][j_42].replace(" ","")
        # Obtencion de las cadenas con un largo mayores a 2        
        if len(derivacion_sin_espacios) > 2:
          cadena_separada = derivacion_sin_espacios[1:]
          #print(cadena_separada)
          # Almacenarlo como un no terminal y su derivacion en la gramatica
          if len(cadena_separada) == 2 and cadena_separada not in partes_cortadas:
            partes_cortadas[cadena_separada] = "C"+str(i_42)
            derivaciones_4.append(cadena_separada)
            nueva_cadena_4 = derivacion_sin_espacios[0] + " C"+str(i_42)
            derivaciones_4[i_42][j_42] = nueva_cadena_4
            #print(derivaciones_4)
          #continuar_cortando = True
  # agregar las nuevas claves a la gramatica original
  for claves_cortadas, valores_cortados in partes_cortadas.items():
    gramatica_4[valores_cortados] = claves_cortadas

  for i_44 in range (len(derivaciones_4)):
    for j_44 in range (len(derivaciones_4[i_44])):
      valores = derivaciones_4[i_44][j_44].replace(" ","")
      for claves_nuevas, valores_nuevas in partes_cortadas.items():
        if claves_nuevas in valores and len(valores) > 2:
          valores_reemplazados = valores.replace(claves_nuevas, valores_nuevas)
          # Agrega la cadena con un espacio entre elementos a la lista
          derivaciones_4[i_44][j_44] = valores_reemplazados[0] + " " + valores_reemplazados[1:]
          #print(derivaciones_4[i_44][j_44])

  for i_43 in range(len(llaves_4)):
    cadena = "|".join(derivaciones_4[i_43])
    gramatica_4[llaves_4[i_43]] = cadena
  #print(gramatica_4)
  return gramatica_4


def opciones():
  seleccion = 0
  repetir = True
  menu = ["Caracteres","Palabras"]
  while repetir:
    print("SELECCIONE UNA DE LAS OPCIONES")
    for i_opc in range (len(menu)):
      print(f"{i_opc+1}. {menu[i_opc]}")
    seleccion = int(input("Ingrese una de las opciones del menu: "))
    if seleccion < 0 or seleccion > len(menu):
      print("DEBE INGRESAR UNA OPCION VALIDA")
    else:
      repetir = False
  return seleccion
