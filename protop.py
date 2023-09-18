import re

def main():
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

        print("\nGramática sin producciones-ε:")
        for produccion in nuevas_producciones:
            print(f"{produccion[0]} -> {produccion[1]}")


# Función para validar una producción de gramática usando una expresión regular
def validar_produccion(produccion):
    #regex = r'^[A-Z]\s*->\s*(ε|[01][A-Z][01]\s*\|\s*)+[A-Z]?'
    regex = r'^[A-Z]\s*->\s*(ε|[01][A-Z][01]\s*\|\s*)*[A-Z]?'
    return re.match(regex, produccion) is not None

# Función para eliminar producciones epsilon
def eliminar_producciones_epsilon(gramatica):
    # Encontrar símbolos anulables
    anulables = set()
    for produccion in gramatica:
        if 'ε' in produccion[1]:
            anulables.add(produccion[0])
    
    # Encontrar las nuevas producciones
    nuevas_producciones = []
    for produccion in gramatica:
        simbolo = produccion[0]
        cuerpo = produccion[1]
        nuevas_cuerpos = ['']
        for c in cuerpo:
            if c in anulables:
                nuevas_cuerpos.extend([nc + c for nc in nuevas_cuerpos])
            else:
                nuevas_cuerpos = [nc + c for nc in nuevas_cuerpos]
        
        for nuevo_cuerpo in nuevas_cuerpos:
            if nuevo_cuerpo != '':
                nuevas_producciones.append((simbolo, nuevo_cuerpo))
    
    return nuevas_producciones

# Cargar la gramática desde un archivo de texto
def cargar_gramatica(nombre_archivo):
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