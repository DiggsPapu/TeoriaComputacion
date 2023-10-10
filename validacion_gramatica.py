import re

def validacion_gramatica(grammars):
    regex_pattern = r'^[\w\s]+->[\w\s\|\$]+$'
    resultados = []

    for production in grammars:
        if re.match(regex_pattern, production):
            #print(f"La producción '{production}' es válida.")
            resultados.append(True)
        else:
            #print(f"La producción '{production}' no es válida.")
            resultados.append(False)
    return resultados

grammars = [
    "S -> NP VP",
    "NP -> Det N",
    "VP -> V NP",
    "Det -> the | a",
    "N -> dog | cat",
    "V -> chased | ate",
]




