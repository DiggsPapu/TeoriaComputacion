from cyk_parse_tree import *
from cfg_implementacion import *
from fileReader import *

def main():
    '''
        En este metodo se inicializa la ejecucion de todo el programa.
    '''
    gramatica_file = "1.txt"
    grammar = cargar_gramatica(gramatica_file)
    
    sin_produccion_epsilon = eliminar_producciones_epsilon(grammar)
    print("SIN PRODUCCIONES EPSILON")
    for clave_sin_epsilon, valor_sin_epsilon in sin_produccion_epsilon.items():
        print(f"{clave_sin_epsilon} -> {valor_sin_epsilon}")

    print("\nSIN PRODUCCIONES UNITARIAS")
    sin_producciones_unitarias = eliminar_producciones_unitarias(sin_produccion_epsilon)
    for clave_sin_unitarias, valor_sin_unitarias in sin_producciones_unitarias.items():
        print(f"{clave_sin_unitarias} -> {valor_sin_unitarias}")
    
    print("\nSIN PRODUCCIONES INUTILES")
    sin_simbolos_inutiles = eliminar_simbolos_inutiles(sin_producciones_unitarias)
    for clave_sin_inutiles, valor_sin_inutiles in sin_simbolos_inutiles.items():
        print(f"{clave_sin_inutiles} -> {valor_sin_inutiles}")
    
    print("\nFORMA NORMAL DE CHOMSKY")
    chomsky = forma_normal_chomsky(sin_simbolos_inutiles)
    for clave_chomsky, valor_chomsky in chomsky.items():
        print(f"{clave_chomsky} -> {valor_chomsky}")
    validacion_sentencias(chomsky)

def validacion_sentencias(gramatica_chomsky):
    '''
        Este metodo tiene como objetivo la validacion de oraciones,
        indicando si tal oracion pertenece o no en la gramatica.

        Args:
        gramatica_sin_chomsky (dict): Diccionario con los elementos no terminales
        y sus respectivas derivaciones
    '''
    gramatica_refactorizada = {}

    for claves_5, valores_5 in gramatica_chomsky.items():       
        gramatica_refactorizada[claves_5] = valores_5.split("|")
    print(f"gramatica refactorizada: {gramatica_refactorizada}")
    while True:
        oracion = str(input("Ingrese una oracion:"))
        print(oracion)
        prueba_cyk(gramatica_refactorizada, oracion.split())
        if not oracion:
            break
    

if __name__ == "__main__":
    main()