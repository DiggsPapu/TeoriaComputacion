import re
# Metodo para cargar la gramatica
def cargar_gramatica(nombre_archivo):
    '''
    Metodo para cargar la gramatica desde un archivo de texto, de manera que debe de estar separado por espacios
    
    Args:
    nombre_archivo (string): ruta del archivo de entrada
    '''
    gramatica = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if validacion_gramatica(linea):
                    linea = linea.replace("Îµ", "ε")
                    simbolo, cuerpo = linea.split('->')
                    productions = cuerpo.split("|")
                    productions = [production.strip() for production in productions]
                    productions = "|".join(productions)
                    gramatica.append(simbolo.strip()+"->"+productions)
                else:
                    print(f"Error: La producción '{linea}' no es válida.")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'.")
    return gramatica
# Metodo que sirve para arreglar la gramatica
def arreglar_gramatica(gramatica:list)->dict:
    '''
    Funcion para arreglar la gramatica dada de manera que la genera en un formato compatible
    
    Args:
    gramatica (list): La gramatica a arreglar
    '''
    structure = {}
    no_terminales = []
    terminales = []
    for regla in gramatica:
        partes = regla.split("->")
        no_terminal = partes[0]
        produccion = partes[1]
        no_terminales.append(no_terminal)
        if no_terminal not in structure.keys():
            structure[no_terminal] = produccion.split("|")
        else:
            structure[no_terminal].extend(produccion.split("|"))
        for production in structure[no_terminal]:
            elementos = production.split(" ")
            todos = []
            for elemento in elementos:
                # Es epsilon
                if elemento == "ε":
                    pass
                # Es no terminal
                elif re.match('[A-Z]+[a-z]*[0-9]*',elemento):
                    no_terminales.append(elemento)
                # Es terminal
                elif re.match('([a-z]*[0-9]*\ ?)+',elemento):
                    terminales.append(elemento)
                    todos.append(1)
            if len(elementos)==len(todos):
                terminales.append(production)
    no_terminales = list(set(no_terminales))
    terminales = list(set(terminales))
    return structure, no_terminales, terminales

# Metodo para validar una gramatica
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