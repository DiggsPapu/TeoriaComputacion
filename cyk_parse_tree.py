import time

class ParseTreeNode:
    def __init__(self, symbol, left=None, right=None, word=None):
        self.symbol = symbol
        self.left = left
        self.right = right
        self.word = word

def cyk_with_parse_tree(grammar, sentence):
    if len(sentence) == 0:
        return None
    else:
        n = len(sentence)
        
        table = [[set() for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for rule, productions in grammar.items():
                for prod in productions:
                    if prod == sentence[i]:
                        table[i][i].add(ParseTreeNode(rule, word=prod))
        
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
        
        if 'E' in [node.symbol for node in table[0][n - 1]]:
            parse_tree = list(table[0][n - 1])[0]
            return parse_tree
        else:
            return None

def prueba_cyk(grammar, sentence):
    #print(f"gramatica refactorizada DOS: {grammar}")
    start_time = time.time()
    parse_tree = cyk_with_parse_tree(grammar, sentence)
    end_time = time.time()
    execution_time = end_time - start_time
    tiempo_en_minutos = execution_time / 60
    tiempo_en_horas = tiempo_en_minutos / 60
    print(f"Tiempo de ejecución: {tiempo_en_horas} horas")
    if parse_tree:
        print("SÍ")
        
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
    grammar = {
        'E': ['T X', 'F Y', 'A C0', 'id'],
        'X': ['C T', 'C C1'],
        'T': ['F Y', 'A C0', 'id'],
        'Y': ['D F', 'D C3'],
        'F': ['A C0', 'id'],
        'A': ['('],
        'B': [')'],
        'C': ['+'],
        'D': ['*'],
        'C0': ['E B'],
        'C1': ['T X'],
        'C3': ['F Y']
    }
    
    # Ingresa la oración entre comillas
    sentence = input("Ingresa una oración: ")
    prueba_cyk(grammar, sentence.split())
'''
'''
{
'E': ['T X', 'F Y', 'A C0', ' id'],
'X': ['C T', 'C C1'], 
'T': ['F Y', 'A C0', ' id'], 
'Y': ['D F', 'D C3'], 
'F': ['A C0', 'id'], 
'A': ['('], 'B': [')'], 
'C': ['+'], 
'D': ['*'], 
'C0': ['E B'], 
'C1': ['T X'], 
'C3': ['F Y']
}
'''