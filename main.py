from cyk_parse_tree import *
from CFG import *
from print import *
from preparation import *

def main():
    '''
        En este metodo se inicializa la ejecucion de todo el programa.
    '''
    grammar = cargar_gramatica("./gramaticas/prueba1.txt")
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
    if gramatica!=None:
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
        validacion_sentencias(gramatica)
    else:
        print("\n_______________________________No se puede trabajar la gramatica___________________________________\n")
if __name__ == "__main__":
    main()