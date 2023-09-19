import re

def main():
  '''
    Metodo para la iniciacion del programa.
  '''
  # Nombre del archivo de entrada con la gramática
  nombre_archivo = "gramatica2.txt"
  #nombre_archivo = "gramatica2.txt"

  # Cargar la gramática
  gramatica = cargar_gramatica(nombre_archivo)

  if gramatica:
    print("Gramática original:")
    for produccion in gramatica:
      print(f"{produccion[0]} -> {produccion[1]}")

    # Eliminar producciones epsilon
    nuevas_producciones = eliminar_producciones_epsilon(gramatica)

    print("\nGramática sin producciones-ε ($):")
    for clave, valor in nuevas_producciones.items():
      print(f"{clave} -> {valor}")

    
    producciones_sin_unitarias = eliminar_producciones_unitarias(nuevas_producciones)
    # eliminar producciones unitarias
    print("\nGramatica sin producciones unitarias: ")
    for clave, valor in producciones_sin_unitarias.items():
      print(f"{clave} -> {valor}")
    
    #producciones_sin_inutiles = eliminar_simbolos_inutiles(producciones_sin_unitarias)
    # eliminar producciones inutiles
    print("\nGramatica sin producciones inutiles: ")
    eliminar_simbolos_inutiles(producciones_sin_unitarias)
  

# Función para validar una producción de gramática usando una expresión regular
def validar_produccion(produccion):
  '''
    Metodo para validar la produccion.
    produccion: str
  '''
  #regex = r'^[A-Z]\s*->\s*(ε|[01][A-Z][01]\s*\|\s*)+[A-Z]?'
  regex = r'^[A-Z]\s*->\s*(ε|[01][A-Z][01]\s*\|\s*)*[A-Z]?'
  return re.match(regex, produccion) is not None

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
  anulables = set()
  for produccion in gramatica:
    if '$' in produccion[1]:
      anulables.add(produccion[0])
  
  # Encontrar las nuevas producciones
  #print(f"anulables: {anulables}")
  nuevas_producciones = []
  resultado = {}
  sin_copias = []
  for produccion in gramatica:
    simbolo = produccion[0]
    #print(f"simbolo: {simbolo}")
    cuerpo = produccion[1].split("|")
    #print(f"cuerpo: {cuerpo}")
    nuevo_cuerpo = []
    # leer cada una de las transiciones
    for derivacion in cuerpo:
      # obtener los no terminales de la lista anulables
      #print(f"derivacion: {derivacion}")
      if "$" in derivacion:
        continue
      else:            
        # depurar los epsilon
        for noTerminal in anulables:
          # Verificar si el no terminal esta en la cadena derivable
          if noTerminal in derivacion:
            # hacer la copia, sin el epsilon
            cadena_modificada = derivacion.replace(noTerminal,"")
            if cadena_modificada != "":
              nuevo_cuerpo.append(derivacion)
              nuevo_cuerpo.append(cadena_modificada)

      nuevo_cuerpo.append(derivacion)
      sin_copias = set(nuevo_cuerpo)
      nuevo_cuerpo = list(sin_copias)
    # almacenar los valores segun sus claves
    nuevas_producciones.append(nuevo_cuerpo)
    
    # volver un diccionario a su estado original 
    for i in range (len(nuevas_producciones)):
      cadena = "|".join(nuevas_producciones[i])
      resultado[simbolo] = cadena
  return resultado

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
  while producciones_unitarias_presentes:
    producciones_unitarias_presentes = False
    for i in range (len(producciones)):
      for j in range (len(producciones[i])):
        for simbolo in simbolos:
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
  resultado = {}
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
  print(diccionario_detallado)
        
          
          
          

  '''
  for i in range (len(producciones)):
    for j in range (len(producciones[i])):
      for k in range (len(simbolos)):
        if simbolos[k] in producciones[i][j]:
          produccion = valores[simbolos[k]]
          for n in range (len(produccion)):
            
            print(producciones[i][j])
  '''
  


        

  
      
    
  
       
    


def forma_normal_chomsky():
  ''''''
  pass

# Cargar la gramática desde un archivo de texto
def cargar_gramatica(nombre_archivo):
  ''''''
  gramatica = []
  try:
    with open(nombre_archivo, 'r') as archivo:
      for linea in archivo:
        linea = linea.strip()
        if validar_produccion(linea):
          simbolo, cuerpo = linea.split('->')
          gramatica.append((simbolo.strip(), cuerpo.strip()))
        else:
          print(f"Error: La producción '{linea}' no es válida.")
  except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'.")
  
  return gramatica


if __name__ == "__main__":
  main()