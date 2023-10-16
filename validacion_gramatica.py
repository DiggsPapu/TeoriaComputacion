import re

def validacion_gramatica(grammars):
    '''
        Metodo para validar si se ingresa una gramatica valida, tanto de manera manual
        como una gramatica directa.

        Args:
        grammars (list): gramatica ingresada. 
    '''
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




