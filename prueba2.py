def cyk_parser(grammar, sentence):
    # Almacenar las palabras en un arreglo
    words = sentence.split()
    # Cantidad de numero de palabras que compone la oracion
    n = len(words)
    # Obtencion de los no terminales de la gramatica
    non_terminals = list(grammar.keys())
    # almacenar los símbolos no terminales que derivan en subcadenas de la cadena de entrada.
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Llenar la diagonal de la tabla con los símbolos terminales
    for i in range(n):
        for non_terminal, productions in grammar.items():
            for production in productions:
                # verifica si alguna producción de la gramática contiene esa palabra
                if words[i] in production.split():
                    # agrega el símbolo no terminal correspondiente a la celda de la tabla.
                    table[i][i].add(non_terminal)

    # Completar la tabla
    # iterar a través de todas las longitudes posibles de subcadenas de la cadena de entrada
    for length in range(2, n + 1):
        # El bucle exterior se ejecuta para todas las longitudes de subcadenas posibles, 
        # y el bucle interior se ejecuta para todas las posiciones de inicio i de una subcadena de esa longitud
        for i in range(n - length + 1):
            j = i + length - 1
            # examinar todas las producciones en la gramática para verificar si A y B 
            # (dos símbolos no terminales) pueden derivar en las subcadenas de la 
            # izquierda (i a k) y derecha (k+1 a j) de una subcadena de longitud length
            for k in range(i, j):
                for non_terminal, productions in grammar.items():
                    for production in productions:
                        # Se hace para todas las producciones de la gramática que tienen dos símbolos no terminales en el lado derecho
                        if len(production.split()) == 2:
                            A, B = production.split()
                            if A in table[i][k] and B in table[k + 1][j]:
                                table[i][j].add(non_terminal)

    # Verificar si la cadena puede ser generada por la gramática
    if 'S' in table[0][n - 1]:
        print("La cadena es generada por la gramática.")
        # Construir el árbol de análisis
        parse_tree = build_parse_tree(table, words, non_terminals)
        print("Árbol de Análisis:")
        print_parse_tree(parse_tree)
    else:
        print("La cadena no es generada por la gramática.")

def build_parse_tree(table, words, non_terminals):
    n = len(words)
    root = Node('S')  # Nodo raíz
    stack = [(root, 0, n - 1)]

    while stack:
        node, i, j = stack.pop()
        if i == j:
            node.add_child(Node(words[i]))
        else:
            for non_terminal, productions in grammar.items():
                for production in productions:
                    if len(production.split()) == 2:
                        A, B = production.split()
                        for k in range(i, j):
                            if A in table[i][k] and B in table[k + 1][j]:
                                childA = Node(A)
                                childB = Node(B)
                                node.add_child(childA)
                                node.add_child(childB)
                                stack.append((childA, i, k))
                                stack.append((childB, k + 1, j))
        return root

def print_parse_tree(node, level=0):
    if node:
        print("  " * level + node.data)
        for child in node.children:
            print_parse_tree(child, level + 1)

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Gramática
grammar = {
    'S': ['NP VP'],
    'VP': ['cooks', 'cuts', 'eats', 'V NP', 'NTERMINAL1 VP1', 'drinks'],
    'PP': ['P NP'],
    'NP': ['Det N', 'he', 'she'],
    'V': ['cooks', 'drinks', 'eats', 'cuts'],
    'P': ['in', 'width'],
    'N': ['cat', 'dog', 'beer', 'cake', 'juice', 'meat', 'soup', 'fork', 'knife', 'oven', 'spoon'],
    'Det': ['a', 'the'],
    'VP1': ['P NP', 'PP VP1'],
    'NTERMINAL1': ['V NP']
}

## Cadena de entrada
#sentence = "he cooks a cake in the oven"

#cyk_parser(grammar, sentence)
