def cyk(grammar, sentence):
    n = len(sentence)
    num_rules = len(grammar)
    
    # Inicializamos la tabla CYK
    table = [[set() for _ in range(n)] for _ in range(n)]
    
    # Llenamos la diagonal de la tabla con las reglas de producción correspondientes a las palabras
    for i in range(n):
        for rule, productions in grammar.items():
            if sentence[i] in productions:
                table[i][i].add(rule)
    
    # Completamos la tabla usando la regla CYK
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for rule, productions in grammar.items():
                    for prod in productions:
                        if len(prod.split()) == 2 and prod.split()[0] in table[i][k] and prod.split()[1] in table[k+1][j]:
                            table[i][j].add(rule)
    
    # Verificamos si la oración pertenece a la gramática
    return 'S' in table[0][n-1]

# Definimos la gramática
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

# Probamos con una oración
sentence = "the dog chased the cat"
result = cyk(grammar, sentence.split())
if result:
    print("La oración pertenece a la gramática.")
else:
    print("La oración no pertenece a la gramática.")
