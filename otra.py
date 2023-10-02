def cyk(grammar, sentence):
    n = len(sentence)
    
    # Inicializamos la tabla CYK
    table = [[set() for _ in range(n)] for _ in range(n)]
    
    # Llenamos la diagonal de la tabla con los símbolos terminales correspondientes a las palabras
    for i in range(n):
        for symbol, words in grammar.items():
            for word in words:
                if sentence[i] == word:
                    table[i][i].add(symbol)
    
    # Completamos la tabla utilizando la regla CYK
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for symbol, productions in grammar.items():
                    for production in productions:
                        if len(production) == 2:
                            A, B = production
                            if A in table[i][k] and B in table[k + 1][j]:
                                table[i][j].add(symbol)
    
    # Verificamos si el símbolo inicial S está en la celda [0][n-1]
    return 'S' in table[0][n - 1]

# Definimos la gramática en CNF
grammar = {
    'S': [('NP', 'VP')],
    'NP': [('Det', 'N')],
    'VP': [('V', 'NP')],
    'Det': ['the', 'a'],
    'N': ['dog', 'cat'],
    'V': ['chased', 'ate']
}

# Probamos con una oración
sentence = ["the", "dog", "chased", "the", "cat"]
result = cyk(grammar, sentence)
if result:
    print("La oración es sintácticamente correcta según la gramática.")
else:
    print("La oración no es sintácticamente correcta según la gramática.")
