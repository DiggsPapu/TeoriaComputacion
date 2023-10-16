import time

class ParseTreeNode:
    '''
        Clase para la construccion del parse Tree
    '''
    def __init__(self, symbol, left=None, right=None, word=None):
        '''
            Constructor para inicializar el parse tree que se utilizara 
            en la demostracion de las derivaciones de la oracion.
        '''
        self.symbol = symbol  # Símbolo de la regla gramatical
        self.left = left      # Nodo hijo izquierdo
        self.right = right    # Nodo hijo derecho
        self.word = word      # Palabra terminal (solo para hojas del árbol)

def cyk_with_parse_tree(grammar, sentence):
    '''
        Implementacion del algoritmo cyk

        Args:
        grammar (dict): Gramatica previamente simplificada.
        sentece (str): oracion que se evaluara en la gramatica.

        Returns:
        None: Si es que pertence o no en la gramatica.
    '''
    if len(sentence) == 0:
        return None
    else:
        n = len(sentence)
        
        # Inicializacion de la tabla CYK con nodos ParseTreeNode
        table = [[set() for _ in range(n)] for _ in range(n)]
        
        # Llenar la diagonal de la tabla con nodos hoja
        for i in range(n):
            for rule, productions in grammar.items():
                for prod in productions:
                    if prod == sentence[i]:
                        table[i][i].add(ParseTreeNode(rule, word=prod))
        
        # Completacion de la tabla usando el algoritmo CYK
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    for rule, productions in grammar.items():
                        for prod in productions:
                            for left_node in table[i][k]:
                                for right_node in table[k + 1][j]:
                                    if left_node.symbol + ' ' + right_node.symbol == prod:
                                        table[i][j].add(ParseTreeNode(rule, left=left_node, right=right_node))
        
        # Verificamos si la oración pertenece a la gramática
        if 'S' in [node.symbol for node in table[0][n - 1]]:
            # Convertir el conjunto en una lista y acceder al primer elemento
            parse_tree = list(table[0][n - 1])[0]
            return parse_tree  # Devolvemos el árbol Parse Tree
        else:
            return None  # La oración no pertenece a la gramática


def prueba_cyk(grammar, sentence):
    '''
        Metodo para realizar la prueba para verificar si una oracion
        pertence a la gramatica.

        Args:
        grammar (dict): Gramatica previamente simplificada.
        sentece (str): oracion a evaluar en la gramatica.
    '''
    start_time = time.time()  # Registrar el tiempo de inicio

    parse_tree = cyk_with_parse_tree(grammar, sentence.split())
    end_time = time.time()  # Registrar el tiempo de finalización
    
    execution_time = end_time - start_time  # Calcular el tiempo de ejecución
    tiempo_en_minutos = execution_time / 60
    tiempo_en_horas = tiempo_en_minutos / 60
    print(f"tiempo de ejecucion: {tiempo_en_horas}")
    if parse_tree:
        print("SÍ")
        
        # Función para imprimir el árbol Parse Tree
        def print_parse_tree(node, level=0):
            if node is not None:
                print('  ' * level + node.symbol)
                if node.word:
                    print('  ' * (level + 1) + node.word)
                else:
                    if node.left:
                        print_parse_tree(node.left, level + 1)
                    if node.right:
                        print_parse_tree(node.right, level + 1)

        print_parse_tree(parse_tree)
    else:
        print("NO")

'''
if __name__ == "__main__":
    # Definicion de una gramatica 
    grammar = {
        'S': ['NP VP'],
        'NP': ['Det N', 'NP PP'],
        'VP': ['V NP', 'VP PP'],
        'PP': ['P NP'],
        'Det': ['the', 'a'],
        'N': ['dog', 'cat', 'bat'],
        'V': ['chased', 'ate', 'saw'],
        'P': ['in', 'on', 'with']
    }
    sentence = "the dog chased the cat"
    prueba_cyk(grammar, sentence)
'''