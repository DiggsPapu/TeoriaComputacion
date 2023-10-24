from cyk_parse_tree import *
from CFG import *
from print import *

def main():
    '''
        En este metodo se inicializa la ejecucion de todo el programa.
    '''
    grammar = cargar_gramatica("./prueba1.txt")
    print("Reglas a trabajar:")
    for rule in grammar:print(" "+rule)
    print("\n___________________________________________________________________________________________________\n")
    gramatica, no_terminales, terminales = arreglar_gramatica(grammar)
    print("Gramatica arreglada: ")
    imprimir_gramatica(gramatica)
    print("No terminales:"+str(no_terminales))
    print("Terminales:"+str(terminales))
    print("\n___________________________________________________________________________________________________\n")
    gramatica = eliminar_producciones_epsilon(gramatica)
    print("Gramatica sin producciones epsilon: ")
    imprimir_gramatica(gramatica)
    print("\n___________________________________________________________________________________________________\n")
    gramatica, no_terminales = eliminar_recursividad(gramatica, no_terminales)
    print("Gramatica sin recursividad:")
    imprimir_gramatica(gramatica)
    print("No terminales:"+str(no_terminales))
    print("\n___________________________________________________________________________________________________\n")
    gramatica = eliminar_producciones_epsilon(gramatica)
    print("Gramatica sin producciones epsilon: ")
    imprimir_gramatica(gramatica)
    print("\n___________________________________________________________________________________________________\n")
    gramatica = remover_producciones_unitarias(gramatica)
    print("Gramatica sin producciones unitarias: ")
    imprimir_gramatica(gramatica)
    print("\n___________________________________________________________________________________________________\n")

    gramatica = remover_producciones_inutiles(gramatica, no_terminales, terminales)
    print("Gramatica sin producciones inutiles: ")
    imprimir_gramatica(gramatica)
    print("\n___________________________________________________________________________________________________\n")
    gramatica = conversion_chomsky(gramatica=gramatica, terminales=terminales)
    print("Gramatica en forma normal de chomsky: ")
    imprimir_gramatica(gramatica)
    print("\n___________________________________________________________________________________________________\n")
    print(gramatica)
    print("\n___________________________________________________________________________________________________\n")
    validacion_sentencias(gramatica)
    
def validacion_sentencias(gramatica_chomsky):
    '''
        Este metodo tiene como objetivo la validacion de oraciones,
        indicando si tal oracion pertenece o no en la gramatica.

        Args:
        gramatica_sin_chomsky (dict): Diccionario con los elementos no terminales
        y sus respectivas derivaciones
    '''
    while True:
        oracion = str(input("Ingrese una oracion: "))
        cyk_parser(gramatica=gramatica_chomsky,enunciado=oracion)
        if str(input("Desea ingresar algun otro enunciado?:S/N: "))!="S":
            break
if __name__ == "__main__":
    main()