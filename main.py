import re

def main():
  '''
    Metodo para la iniciacion del programa.
  '''
  # Nombre del archivo de entrada con la gramática
  nombre_archivo = "gramatica1.txt"
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

    

    # eliminar producciones unitarias
    print("\nGramatica sin producciones unitarias: ")
   # producciones_sin_unitarias = 
  eliminar_producciones_unitarias(nuevas_producciones)

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
      
    #print(f"nuevo cuerpo: {nuevo_cuerpo}")
    # almacenar los valores segun sus claves
    nuevas_producciones.append(nuevo_cuerpo)
    # volver un diccionario a su estado original 
    for i in range (len(nuevas_producciones)):
      cadena = "|".join(nuevas_producciones[i])
      resultado[simbolo] = cadena
  #print(f"nueva produccion: {nuevas_producciones}")
  #print(resultado)
  return resultado

def eliminar_producciones_unitarias(gramatica):
  '''
  '''
  simbolo = []
  producciones = []

  for clave, valor in gramatica.items():
    print(f"{clave} -> {valor}")
    simbolo.append(clave)
    producciones.append(valor.split("|"))
  



def eliminar_simbolos_inutiles():
  ''''''
  pass

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