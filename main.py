from validacion_gramatica import validacion_gramatica
from cyk_implementacion import cyk
from cyk_parse_tree import *
from cfg_implementacion import *

def main():
    '''
        En este metodo se inicializa la ejecucion de todo el programa.
    '''
    
    grammar = [
        "S->NP|VP",
        "VP->VP|PP",
        "VP->V|NP",
        "VP->cooks|drinks|eats|cuts",
        "PP->P|NP",
        "NP->Det|N",
        "NP->he|she",
        "V->cooks|drinks|eats|cuts",
        "P->in|with|$",
        "N->cat|dog",
        "N->beer|cake|juice|meat|soup",
        "N->fork|knife|oven|spoon",
        "Det->a|the",
    ]
    
    #grammar = gramatica_input()
    
    gramatica = arreglar_gramatica(grammar)
    #print(gramatica)
    validaciones = validacion_gramatica(gramatica)
    if False in validaciones:
        print("La gramatica no es valida.")
    else:
        sin_produccion_epsilon = eliminar_producciones_epsilon(gramatica)
        #print(f"sin producciones epsilon: {sin_produccion_epsilon}")
        sin_producciones_unitarias = eliminar_producciones_unitarias(sin_produccion_epsilon)
        #print(f"sin producciones unitarias",sin_producciones_unitarias)
        sin_simbolos_inutiles = eliminar_simbolos_inutiles(sin_producciones_unitarias)
        #print(f"sin simbolos inutiles: {sin_simbolos_inutiles}")
        chomsky, gramatica_sin_chomsky = forma_normal_chomsky(sin_simbolos_inutiles)
        #print(f"Formal normal de chomsky: {chomsky}")
        validacion_sentencias(gramatica_sin_chomsky)
        
        
        

def arreglar_gramatica(gramatica):
    '''
        Esta función toma una lista de reglas de gramática y las reorganiza
        de manera que los no terminales se agrupen y no se repitan.

        Args:
        gramatica (list): Una lista de reglas de gramática en formato "A -> B|C|D".

        Returns:
        list: Una nueva lista de reglas de gramática con no terminales agrupados.
    '''
    # Crea un diccionario para almacenar las producciones de cada no terminal
    producciones = {}

    # Recorre las reglas de la gramática
    for regla in gramatica:
        partes = regla.split("->")
        no_terminal = partes[0]
        produccion = partes[1]

        # Si el no terminal ya existe en el diccionario, agrega la producción
        if no_terminal in producciones:
            producciones[no_terminal].extend(produccion.split("|"))
        else:
            producciones[no_terminal] = produccion.split("|")

    # Crea una nueva lista de reglas con las producciones agrupadas
    nueva_gramatica = []
    for no_terminal, produccion in producciones.items():
        nueva_gramatica.append(f"{no_terminal}->{'|'.join(produccion)}")
    return nueva_gramatica

def gramatica_input():
    '''
        Este metodo sirve para poder ingresar de manera manual la gramatica
        que servira para el ejercicio.

        Returns:
        list: los elementos de la gramatica que se han ingresado de manera manual
    '''
    # Inicializa una lista vacía para almacenar las reglas de producción
    gramatica_entrada = []
    # Lee las reglas de producción desde la consola hasta que el usuario ingrese una línea en blanco
    while True:
        input_line = input("Ingrese una regla de producción (o presione Enter para finalizar): ")
        if not input_line:
            break
        gramatica_entrada.append(input_line.strip())
    return gramatica_entrada

def validacion_sentencias(gramatica_sin_chomsky):
    '''
        Este metodo tiene como objetivo la validacion de oraciones,
        indicando si tal oracion pertenece o no en la gramatica.

        Args:
        gramatica_sin_chomsky (dict): Diccionario con los elementos no terminales
        y sus respectivas derivaciones
    '''
    gramatica_refactorizada = {}

    for claves_5, valores_5 in gramatica_sin_chomsky.items():       
        gramatica_refactorizada[claves_5] = valores_5.split("|")
    #print(gramatica_refactorizada)
    while True:
        oracion = str(input("Ingrese una oracion: "))
        prueba_cyk(gramatica_refactorizada, oracion)
        if not oracion:
            break
    

if __name__ == "__main__":
    main()