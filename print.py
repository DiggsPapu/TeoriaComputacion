def imprimir_gramatica(gramatica: dict):
    '''
    Funcion para imprimir la gramatica en cierto formato
    
    Args:
    gramatica (dict): gramatica a imprimir
    '''
    for no_terminal, production in gramatica.items():
        production_string = "|".join(production)
        print(f"    {no_terminal} -> {production_string}")

def print_tree(tree, level=0):
    '''
    Funcion para imprimir el arbol
    
    Args:
    tree (Node): Nodo raiz del arbol
    level (int): nivel actual del nodo
    '''
    if tree is not None:
        print("  " * level + tree.label)
        for child in tree.children:
            print_tree(child, level + 1)