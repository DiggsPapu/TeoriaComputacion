# Estructura para hacer el arbol
class ParseTree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []
        
# El algoritmo de CYK  
def cyk_parser(gramatica:dict, enunciado:str):
    no_terminal_initial:str = list(gramatica.keys())[0]
    palabras = enunciado.split()
    n = len(palabras)
    tabla = [[set() for _ in range(n)] for _ in range(n)]
    # Llenar la diagonal con las palabras, de manera que si existen entonces se aniade
    for i in range(n):
        for non_terminal, productions in gramatica.items():
            for production in productions:
                if palabras[i] in production.split():
                    tabla[i][i].add(non_terminal)
    # Completar la tabla
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for non_terminal, productions in gramatica.items():
                    for production in productions:
                        if len(production.split()) == 2:
                            A, B = production.split()
                            if A in tabla[i][k] and B in tabla[k + 1][j]:
                                tabla[i][j].add(non_terminal)
    # # Verificar si la cadena puede ser generada por la gramática
    if no_terminal_initial in tabla[0][n - 1]:
        print("SI")
        start_symbol = list(gramatica.keys())[0]
        parse_tree = construct_parse_tree(tabla, gramatica, start_symbol, enunciado.split())
        print_tree(parse_tree)
        build_graphviz_tree(parse_tree)
    else:
        print("NO")
        
def build_tree(i, j, non_terminal, gramatica, palabras, tabla):
        if i == j:
            for production in gramatica[non_terminal]:
                elements = production.split(" ")
                if palabras[i] in elements:
                    palabra = ParseTree(palabras[i])
                    return ParseTree(non_terminal, [palabra])
                elif len(elements)>1:
                    for element in elements:
                        if palabras[i] in gramatica[element]:
                            palabra = ParseTree(palabras[i])
                            return ParseTree(element, [palabra])
        else:
            for k in range(i, j):
                for production in gramatica[non_terminal]:
                    if len(production.split()) == 2:
                        A, B = production.split()
                        if A in tabla[i][k] and B in tabla[k + 1][j]:
                            left_tree = build_tree(i, k, A, gramatica, palabras, tabla)
                            right_tree = build_tree(k + 1, j, B, gramatica, palabras, tabla)
                            return ParseTree(non_terminal, [left_tree, right_tree])
                        
def construct_parse_tree(tabla, gramatica, start_symbol, palabras):
    # Longitud
    n = len(palabras)    
    if tabla != None:
        # Construye mediante recursividad el arbol
        return build_tree(0, n - 1, start_symbol, gramatica, palabras, tabla)
    else:
        # Si es una tabla invalida entonces retorna None
        return None
# Es para generar el .dot en el archivo
def write_node(node:ParseTree, file, nodes_def="",nodes_connection="", nodes_already = []):
    # Esto sirve porque en el caso de que sean nodos ya usados para generar una palabra en especifico pero se requiere que se vuelvan a usar entonces se usa esto.
    amount_sucesions = nodes_already.count(node.label)
    if amount_sucesions>0:
        nodes_def += node.label+"_"+str(amount_sucesions+1)+" [shape=circle] [label=\""+node.label+"\"];\n"
        nodes_already.append(node.label)
        if len(node.children)>0:
            for child in node.children:
                amount_sucesions2 = nodes_already.count(child.label)
                if amount_sucesions2>0:
                    nodes_connection+=node.label+"_"+str(amount_sucesions+1)+"->"+child.label+"_"+str(amount_sucesions2+1)+";\n"
                    nodes_def, nodes_connection = write_node(child,file,nodes_def,nodes_connection)
                else:
                    nodes_connection+=node.label+"_"+str(amount_sucesions+1)+"->"+child.label+";\n"
                    nodes_def, nodes_connection = write_node(child,file,nodes_def,nodes_connection)
    else:
        nodes_def += node.label+" [shape=circle] [label=\""+node.label+"\"];\n"
        nodes_already.append(node.label)
        if len(node.children)>0:
            for child in node.children:
                amount_sucesions2 = nodes_already.count(child.label)
                if amount_sucesions2>0:
                    nodes_connection+=node.label+"->"+child.label+"_"+str(amount_sucesions2+1)+";\n"
                    nodes_def, nodes_connection = write_node(child,file,nodes_def,nodes_connection)
                else:
                    nodes_connection+=node.label+"->"+child.label+";\n"
                    nodes_def, nodes_connection = write_node(child,file,nodes_def,nodes_connection)
    # Son strings para hacer la definicion de los nodos y a que lados estan conectados los nodos
    return nodes_def, nodes_connection
# Construccion del arbol graphviz
def build_graphviz_tree(tree:ParseTree):
    # Realiza manualmente la creacion del dot, sin librerias.
    with open("./parse_tree.dot", 'w') as file:
        file.write("digraph AFD{\nnode [shape=circle];\nrankdir=UD;\n")
        nodes_def, nodes_connection = write_node(tree,file)
        file.write(nodes_def)
        file.write(nodes_connection)
        file.write("}\n")
        
def print_tree(tree, level=0):
    if tree is not None:
        print("  " * level + tree.label)
        for child in tree.children:
            print_tree(child, level + 1)

# Gramática
# gramatica = {
#     "S": ["NP VP"],
#     "VP": ["cooks", "cuts", "eats", "V NP", "NTERMINAL1 VP1", "drinks"],
#     "PP": ["P NP"],
#     "NP": ["Det N", "he", "she"],
#     "V": ["cooks", "drinks", "eats", "cuts"],
#     "P": ["in", "width"],
#     "N": ["cat", "dog", "beer", "cake", "juice", "meat", "soup", "fork", "knife", "oven", "spoon"],
#     "Det": ["a", "the"],
#     "VP1": ["P NP", "PP VP1"],
#     "NTERMINAL1": ["V NP"]
# }
# gramatica = {'S': ['NP VP'], 'VP': ['cooks', 'drinks', 'V NP', 'eats', 'cuts', 'NTERMINAL1 VP1'], 'PP': ['P NP'], 'NP': ['Det N', 'he', 'she'], 'V': ['cooks', 'drinks', 'eats', 'cuts'], 'P': ['in', 'width'], 'N': ['cat', 'dog', 'beer', 'cake', 'juice', 'meat', 'soup', 'fork', 'knife', 'oven', 'spoon'], 'Det': ['a', 'the'], 'VP1': ['PP VP1', 'P NP'], 'NTERMINAL1': ['V NP']}

# # Cadena de entrada
# enunciado = "he cooks a cake in the oven"

# cyk_parser(gramatica, enunciado)


# Usage
# gramatica = {
#     "S": ["NP VP", "S and S", "P S"],
#     "NP": ["I", "he", "she"],
#     "VP": ["reads", "eats", "sleeps"],
#     "P": ["before", "after"],
# }

# enunciado = "he cooks a cake in the oven"


