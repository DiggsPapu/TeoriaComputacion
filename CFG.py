import re
import copy
def arreglar_gramatica(gramatica:list)->dict:
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
def eliminar_recursividad(gramatica:dict, no_terminales:list):
    new_no_terminales = copy.deepcopy(no_terminales)
    # Idea: encontrar todos los posibles recursivos y almacenarlos en una lista y luego operarlos
    recursivos = {}
    betas = {}
    for no_terminal, productions in gramatica.items():
        for production in productions:
            elementos = production.split(" ")
            # Si la produccion es recursiva inmediatamente y tiene un alfa entonces se aniade a mi lista de producciones recursivas
            if elementos[0]==no_terminal and len(elementos)>1 and no_terminal not in recursivos.keys():
                recursivos[no_terminal]=[production]
            elif elementos[0]==no_terminal and len(elementos)>1:
                recursivos[no_terminal].append(production)
            # Si la produccion no es recursiva y la lista de recursivos no esta vacia se puede usar como una produccion beta
            elif elementos[0]!=no_terminal and no_terminal not in betas.keys():
                betas[no_terminal]=[production]
            elif elementos[0]!=no_terminal:
                betas[no_terminal].append(production)
    # Si al menos existe una produccion beta para cada produccion recursiva entonces se puede hacer el algoritmo de eliminacion 
    print("recursivos:"+str(recursivos))
    print("betas:"+str(betas))
    for no_terminal, productions in recursivos.items():
        if len(recursivos[no_terminal])<=len(betas[no_terminal]):
            index = 0
            new_no_terminal = no_terminal+str(1)
            for production in productions:
                # Remuevo la produccion recursiva
                gramatica[no_terminal].remove(production)
                # Remuevo la produccion beta a usar
                gramatica[no_terminal].remove(betas[no_terminal][index])
                # Aniado la nueva produccion en este terminal
                new_p_nt = betas[no_terminal][index]+" "+new_no_terminal
                gramatica[no_terminal].append(new_p_nt)
                # crear el alfa
                elementos:list = production.split(" ")
                elementos.pop(0)
                elementos = " ".join(elementos)
                alpha = elementos+" "+new_no_terminal
                if new_no_terminal not in gramatica.keys():
                    gramatica[new_no_terminal]=[alpha,"ε"]
                    new_no_terminales.append(new_no_terminal)
                else:
                    gramatica[new_no_terminal].append(alpha)
                index+=1
        else:
            print("No se puede eliminar la recursividad en la gramatica porque no se poseen suficientes betas")
            return None, new_no_terminales
        
    return gramatica, new_no_terminales

def recursividad_parejas_unarias(gramatica:dict, parejas_unarias:list, unary_pair:tuple, no_terminales:list):
    for production in gramatica[unary_pair[1]]:
        if unary_pair[1] != production and production in no_terminales:
            new_p = (unary_pair[1],production)
            if new_p not in parejas_unarias:
                parejas_unarias.append(new_p)
                parejas_unarias = recursividad_parejas_unarias(gramatica,parejas_unarias,new_p, no_terminales)
    return parejas_unarias
def crear_parejas_unarias(gramatica:dict):
    parejas_unarias = []
    no_terminales = gramatica.keys()
    for no_terminal, productions in gramatica.items():
        for production in productions:
            # Es unaria si esta en el conjunto de no terminales
            if production in no_terminales and no_terminal!=production:
                unary_pair = (no_terminal, production)
                if unary_pair not in parejas_unarias:
                    parejas_unarias.append(unary_pair)
                # Transitividad
                recursividad_parejas_unarias(gramatica, parejas_unarias, unary_pair, no_terminales)
                for X, Y in parejas_unarias:
                    new_ = (X, production)
                    if Y == no_terminal and new_ not in parejas_unarias and X!=production:
                        parejas_unarias.append(new_)
            elif no_terminal == production:
                gramatica[no_terminal].remove(production)
    return parejas_unarias, gramatica
def remover_producciones_unitarias(gramatica:dict):
    parejas_unarias, gramatica = crear_parejas_unarias(gramatica)
    print("Parejas unitarias:"+str(parejas_unarias))
    for no_t1, no_t2 in parejas_unarias:
        # Esta en las producciones no transitiva
        try:
            gramatica[no_t1].remove(no_t2)
        except:
            pass
    gramatica_new = gramatica.copy()
    for no_t1, no_t2 in parejas_unarias:
        gramatica_new[no_t1].extend(gramatica[no_t2])
        gramatica_new[no_t1] = list(set(gramatica_new[no_t1]))
    return gramatica_new

def index_ocurrencia_elemento(lista:list, element:str, occurrence_number:int):
    found_count = 0
    for index, item in enumerate(lista):
        if item == element:
            found_count += 1
            if found_count == occurrence_number:
                return index
    return -1  # Element not found for the specified occurrence.
def generar_producciones_epsilon(elementos:list, elemento_anulable:str, cantidad_ocurrencias:int, epsilon_productions:list = [], num_oc:int=1):
    if num_oc<=cantidad_ocurrencias:
        copy_list = elementos.copy()
        copy_list.pop(index_ocurrencia_elemento(lista=elementos, element=elemento_anulable,occurrence_number=num_oc))
        epsilon_productions.append(" ".join(copy_list))
        epsilon_productions = generar_producciones_epsilon(elementos=elementos,elemento_anulable=elemento_anulable,epsilon_productions=epsilon_productions,num_oc=num_oc+1,cantidad_ocurrencias=cantidad_ocurrencias)
        epsilon_productions = list(set(epsilon_productions))
        for production in epsilon_productions:
            elements = production.split(" ")
            index = index_ocurrencia_elemento(lista=elements, element=elemento_anulable,occurrence_number=num_oc)
            if index!=-1:
                elements.pop(index)
                new_p = " ".join(elements)
                if new_p not in epsilon_productions:
                    epsilon_productions.append(new_p)
            # En caso de que se generen todas las permutaciones posibles
            if len(epsilon_productions)==2^cantidad_ocurrencias:
                break
    try:
        epsilon_productions.remove('')
    except:
        pass
    return epsilon_productions
    
def eliminar_producciones_epsilon(gramatica:dict):
    anulables = []
    # Identificar las producciones epsilon y remover las producciones epsilon
    for no_terminal in gramatica.keys():
        if "ε" in gramatica[no_terminal]:
            # Aniado los que son no anulables a una lista de no anulables
           anulables.append(no_terminal)
           gramatica[no_terminal].remove("ε")
    
    
    for no_terminal, productions in gramatica.items():
        for production in productions:
            elementos = production.split(" ")
            elementos_evaluados = []
            for elemento in elementos:   
                        #  Si es anulable y no ha sido evaluado
                    if elemento in anulables and elemento not in elementos_evaluados:
                        cantidad_ocurrencias = elementos.count(elemento)
                        if cantidad_ocurrencias>1:
                            # Se aniade la produccion 1
                            epsilon_productions = [production]
                            epsilon_productions = generar_producciones_epsilon(elementos=elementos,elemento_anulable=elemento,epsilon_productions=epsilon_productions,cantidad_ocurrencias=cantidad_ocurrencias)
                            gramatica[no_terminal].extend(epsilon_productions)
                            gramatica[no_terminal] = list(set(gramatica[no_terminal]))
                            elementos_evaluados.append(elemento)
                        elif cantidad_ocurrencias == 1:
                            n_p = elementos.copy()
                            n_p.remove(elemento)
                            n_p = " ".join(n_p)
                            if n_p!='':
                                gramatica[no_terminal].append(n_p)
                                elementos_evaluados.append(elemento)
                                gramatica[no_terminal] = list(set(gramatica[no_terminal]))
    return gramatica                   


def es_alcanzable(gramatica:dict, no_terminales:list, no_terminal:str, no_terminal_inicial:str, producciones_exploradas:list): 
    producciones_exploradas = list(set(producciones_exploradas))
    # Si el no terminal inicial no esta en las producciones exploradas entonces este no terminal y sus producciones no han sido explorados
    if no_terminal_inicial not in producciones_exploradas:
        producciones_exploradas.append(no_terminal_inicial)
        try:
            for production in gramatica[no_terminal_inicial]:
                elementos = production.split(" ")
                if no_terminal in elementos:
                    return True
                else:
                    for elemento in elementos:
                        if elemento in no_terminales:
                            if es_alcanzable(gramatica, no_terminales, no_terminal, elemento,producciones_exploradas):
                                return True
        except:
            # Significa que ni siquiera tiene producciones asignadas, por ende es inalcanzable
            return False
    return False

def produccion_es_util(production:str, no_terminales:list, gramatica:dict, reglas_utiles:dict, terminales:list, no_terminales_explorados:list=[]):
    # Una produccion puede estar compuesta por terminales y no terminales entonces se debe de separar en elementos
    elements = production.split(" ")
    # Si tiene un solo elemento -> es una sola produccion y es un terminal
    if len(elements)==1 and elements[0] in terminales:
        return True, reglas_utiles
    # Si no esta en la gramatica entonces no tiene producciones
    elif len(elements)==1 and elements[0] not in gramatica.keys() and elements[0] in no_terminales:
        return False, reglas_utiles
    # Si esta en la gramatica entonces tiene producciones
    elif len(elements)==1 and elements[0] in gramatica.keys():
        # Si ya se calculo retornar si es util o no y la regla util
        if elements[0] in reglas_utiles.keys():
            return reglas_utiles[element], reglas_utiles
        else:
            # Calcular si es util
            util, reglas_utiles = produccion_es_util(production=gramatica[element],no_terminales=no_terminales,gramatica=gramatica,reglas_utiles=reglas_utiles,terminales=terminales)
            reglas_utiles[element].append(util)
            return util, reglas_utiles
    # Si no tiene elementos entonces no es util
    elif len(elements)==0:
        return False, reglas_utiles
    # Tiene varios elementos en el terminal hay que chequear si todos son terminales e ir a buscar si lleva a algun no terminal valido
    all_terminals = []
    for element in elements:
        # Si es terminal todo bien
        if element in terminales:
            all_terminals.append(True)            
        # Tiene al menos una produccion no terminal entonces se requiere de recursion para chequear a donde lleva y si retorna un terminal entonces se puede seguir chequeando si no no
        # el diccionario sirve para determinar si llega a algo o no, ademas se tendra que usar recursion si en el diccionario no ha sido calculado aun
        elif element in no_terminales and element in reglas_utiles.keys() and element not in no_terminales_explorados:
            # Si ya se calculo si una regla con cierto no_terminal es util entonces se usa esto para calcular y por ende no es necesario meterlo en explorados
            if len(reglas_utiles[element])>0:
                all_terminals.append(reglas_utiles[element][0])
            # Si no se ha calculado
            else:
                for prod in gramatica[element]:
                    # Se calcula si es una produccion util
                    no_terminales_explorados.append(element)
                    util, reglas_utiles = produccion_es_util(production=prod,no_terminales=no_terminales,gramatica=gramatica,reglas_utiles=reglas_utiles,terminales=terminales,no_terminales_explorados=no_terminales_explorados)
                    all_terminals.append(util)
                    reglas_utiles[element].append(util)
        # Dado que no esta en reglas utiles
        elif element not in no_terminales_explorados and element in no_terminales and element not in reglas_utiles.keys():
            for prod in gramatica[element]:
                util, reglas_utiles = produccion_es_util(
                production=prod,
                no_terminales=no_terminales,
                gramatica=gramatica,
                reglas_utiles=reglas_utiles,
                terminales=terminales
                )
                all_terminals.append(util)
                reglas_utiles[element] = util
                
        elif element in no_terminales:
            for prod in gramatica[element]:
                util, reglas_utiles = produccion_es_util(production=gramatica[element],no_terminales=no_terminales,gramatica=gramatica,reglas_utiles=reglas_utiles,terminales=terminales)
                all_terminals.append(util)
                reglas_utiles[element].append(util)
        elif element in no_terminales_explorados:
            return False, reglas_utiles
        # Su regla no ha sido creada entonces toca calcular
    # Compuesto full de terminales
    if False in all_terminals:
        return False
    return True

def prod_util(no_terminal_inicial:str, gramatica:dict, reglas_utiles:dict, no_terminales:list, terminales:list, no_terminales_explorados:list):
    s_terminales = set(terminales)
    s_productions = set(gramatica[no_terminal_inicial])
    # si tiene al menos una terminal entonces es una produccion util
    if s_terminales.intersection(s_productions):
        return True
    # Si no se ha evaluado aun
    if no_terminal_inicial not in no_terminales_explorados:
        no_terminales_explorados.append(no_terminal_inicial)
        # Si no tiene al menos una entonces hay que derivar su regla para ver si al menos hay una produccion que genere
        for production in gramatica[no_terminal_inicial]:
            if production in list(reglas_utiles.keys()):
                return reglas_utiles[production]
            elif production in terminales:
                return True
            else:
                elementos = production.split(" ")
                eval = []
                for element in elementos:
                    if element in terminales:
                        eval.append(True)
                    elif element in list(reglas_utiles.keys()):
                        eval.append(reglas_utiles[element])
                    else:
                        value = prod_util(no_terminal_inicial=element,gramatica=gramatica,reglas_utiles=reglas_utiles,no_terminales=no_terminales,terminales=terminales,no_terminales_explorados=no_terminales_explorados)
                        if value:
                            eval.append(True)
                        # No es una produccion valida pasar a la siguiente regla a evaluar
                        else:
                            break
                if False in eval:
                    pass
                else:
                    return True
    # En caso de que se evalue todo y no llegue a nada
    return False

def remover_producciones_inutiles(gramatica:dict, no_terminales:list, terminales:list):
    reglas_utiles = {}
    # Se supone que es el primero
    no_terminal_inicial = list(gramatica.keys())[0]
    gramatica_new = copy.deepcopy(gramatica)
    no_terminales_new = list(gramatica.keys())
    no_terminales_inproductivos = []
    # Voy a determinar todos los no terminales en la gramatica que deriven a algo
    for no_terminal, productions in gramatica.items():
        s_productions = set(productions)
        s_terminales = set(terminales)
        if len(s_productions.intersection(s_terminales))>0 or no_terminal_inicial==no_terminal: # tiene al menos un no terminal por ende es util
            reglas_utiles[no_terminal] = True
    # Se eliminan los no productivos
    for no_terminal, productions in gramatica.items():
        if len(productions)==1:
            elementos = productions[0].split(" ")
            # No produce nada es inutil
            if no_terminal in elementos:
                gramatica_new.pop(no_terminal)
                no_terminales_inproductivos.append(no_terminal)
        else:
            for production in productions:
                elementos = production.split(" ")
                if production in terminales:
                    pass 
                # Es un simbolo inutil
                elif production not in terminales and production in no_terminales and production not in gramatica.keys():
                    gramatica_new[no_terminal].remove(production)
                    no_terminales_inproductivos.append(production)
                elif len(elementos)>1 and production not in terminales:
                    for element in elementos:
                        if element in no_terminales and element not in gramatica.keys() or element in no_terminales_inproductivos:
                            gramatica_new[no_terminal].remove(production)
                            reglas_utiles[element] = False
                            no_terminales_inproductivos.append(element)
                            break
    gramatica = copy.deepcopy(gramatica_new)
    reglas_a_evaluar = list(set(gramatica_new.keys()).difference(reglas_utiles.keys()))
    # Se eliminan los no productivos en caso de que sea un no terminal en mas de un paso  
    for no_terminal in reglas_a_evaluar:
        productions = gramatica_new[no_terminal]
        if len(productions)==1:
            elements = productions[0].split(" ")
            # Nunca producira algo, se remueve
            if no_terminal in elements:
                gramatica_new.pop(no_terminal)
                reglas_utiles[no_terminal]=False
                no_terminales_inproductivos.append(no_terminal)
            else:
                eval = []
                for element in elements:
                    if element in terminales:
                        eval.append(True)
                    elif element in reglas_utiles.keys():
                        eval.append(reglas_utiles[element])
                    # Peor de los casos se tiene que hacer recursion
                    else:
                        value = prod_util(
                            no_terminal_inicial=element,
                            gramatica=gramatica,
                            reglas_utiles=reglas_utiles,
                            no_terminales=no_terminales,
                            terminales=terminales,
                            no_terminales_explorados=[])
                        if value:
                            eval.append(value)
                        # Esta produccion no vale y por ende la regla tampoco
                        else:
                            gramatica_new.pop(no_terminal)
                            reglas_utiles[no_terminal]=False
                            no_terminales_inproductivos.append(no_terminal)
                            break
                if False in eval:
                    gramatica_new.pop(no_terminal)
                    reglas_utiles[no_terminal]=False
                    no_terminales_inproductivos.append(no_terminal)
                reglas_utiles[no_terminal]=True
        else:
            for prod in gramatica_new[no_terminal]:
                elements = prod.split(" ")
                eval = []
                for element in elements:
                    if element in terminales:
                        eval.append(True)
                    # No sirve para evaluar si es productivo pero si para eliminarlo de la gramatica
                    elif element in no_terminales_inproductivos:
                        gramatica_new[no_terminal].remove(prod)
                        break
                    elif element in list(reglas_utiles.keys()):
                        if reglas_utiles[element]:
                            eval.append(True)
                        # Esta produccion no me sirve pasa a la siguiente
                        else:
                            gramatica_new[no_terminal].remove(prod)
                            break
                    # Esta produccion no nos sirve para valuar si es util o no
                    elif element == no_terminal:
                        break
                    else:
                        value = prod_util(
                            no_terminal_inicial=element,
                            gramatica=gramatica,
                            reglas_utiles=reglas_utiles,
                            no_terminales=no_terminales,
                            terminales=terminales,
                            no_terminales_explorados=[])
                        if value:
                            eval.append(value)
                        # Esta produccion no vale
                        else:
                            gramatica_new[no_terminal].remove(prod)
                            break
                if False not in eval and len(eval)==len(elements):
                    reglas_utiles[no_terminal]=True
                    
    items_gramatica = copy.deepcopy(list(gramatica_new.items()))
    for no_terminal, productions in items_gramatica:
        for production in productions:
            elementos = production.split(" ")
            for elemento in elementos:
                if elemento in no_terminales_inproductivos:
                    # eliminar produccion
                    gramatica_new[no_terminal].remove(production)
    gramatica_new2 = copy.deepcopy(gramatica_new)
    for no_terminal, production in gramatica_new2.items():
        for production in productions:
            # Si no es el terminal inicial
           if no_terminal != no_terminal_inicial:
                # Es alcanzable
                producciones_exploradas = []
                es_alcanzable_ = es_alcanzable(gramatica_new2, no_terminales, no_terminal, no_terminal_inicial, producciones_exploradas)
                # Se remueve porque no es alcanzable y no es el terminal inicial
                if not es_alcanzable_:
                    gramatica_new.pop(no_terminal)
    return gramatica_new

def conversion_chomsky(gramatica:dict, terminales:list):
    # Paso 1 convertir todas las producciones con terminales de longitud n>2 a no terminales
    gramatica_new = copy.deepcopy(gramatica)
    terminales_trabajados = {}
    for no_terminal, productions in gramatica.items():
        for index_p in range(len(productions)):
            production = productions[index_p]
            elements = production.split(" ")
            if len(elements)>1:
                for index in range(len(elements)):
                    element = elements[index]
                    # Es un terminal y no se le ha hecho un no terminal
                    if element in terminales and element not in terminales_trabajados.keys():
                        new_non_terminal = "TERMINAL"+str(len(terminales_trabajados)+1)
                        gramatica_new[new_non_terminal] = [element]
                        terminales_trabajados[element] = new_non_terminal
                        # Creo la produccion nueva
                        new_production = copy.deepcopy(gramatica_new[no_terminal][index_p])
                        new_production = new_production.split(" ")
                        new_production.pop(index)
                        new_production.insert(index, new_non_terminal)
                        # Remuevo la produccion anterior
                        gramatica_new[no_terminal].pop(index_p)
                        gramatica_new[no_terminal].insert(index_p," ".join(new_production))
                    elif element in terminales:
                        # Creo la produccion nueva
                        new_production = copy.deepcopy(gramatica_new[no_terminal][index_p])
                        new_production = new_production.split(" ")
                        new_production.pop(index)
                        new_production.insert(index, terminales_trabajados[element])
                        # Remuevo la produccion anterior
                        gramatica_new[no_terminal].pop(index_p)
                        gramatica_new[no_terminal].insert(index_p," ".join(new_production))
    # print(gramatica_new)      
    # print("_________________________________________________________")     
    # Paso 2 reducir longitudes
    gramatica = copy.deepcopy(gramatica_new)
    no_terminales_trabajados = {}
    for no_terminal, productions in gramatica.items():
        for index_p in range(len(productions)):
            production = productions[index_p]
            elements = production.split(" ")
            
            if len(elements)>2:
                elementos = copy.deepcopy(elements)
                # Mientras la longitud sea mayor que 2                    
                while len(elementos)>2:
                    elemento_1 = elementos[0]
                    elemento_2 = elementos[1]
                    concat = elemento_1+" "+elemento_2
                    if concat not in no_terminales_trabajados.keys():
                        new_non_terminal = "NTERMINAL"+str(len(no_terminales_trabajados)+1)
                        gramatica_new[new_non_terminal] = [concat]
                        # Se elimina el elemento 0 y 1
                        elementos.pop(0)
                        elementos.pop(0)
                        # Se agrega el nuevo no terminal
                        elementos.insert(0, new_non_terminal)
                        no_terminales_trabajados[concat] = new_non_terminal
                    elif concat in no_terminales_trabajados.keys():
                        # Se elimina el elemento 0 y 1
                        elementos.pop(0)
                        elementos.pop(0)
                        # Se agrega el no terminal
                        elementos.insert(0, no_terminales_trabajados[concat])
                gramatica_new[no_terminal].pop(index_p)
                gramatica_new[no_terminal].insert(index_p, " ".join(elementos))
        
    # print(gramatica_new)
    return gramatica_new

def cargar_gramatica(nombre_archivo):
    ''''''
    gramatica = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if validacion_gramatica(linea):
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

def otro_formato(gramatica:dict):
    new_gramatica = {}
    for no_terminal, productions in gramatica.items():
        new_gramatica[no_terminal]="|".join(productions)
    print(new_gramatica)
    return new_gramatica
# YA PASO ESTA GRAMATICA, NO SE PUEDE TRABAJAR PORQUE AL REMOVER LOS EPSILON NO SE POSEEN SUFICIENTES BETAS
# grammar = [
#     "E->E + T|T",
#     "T->T * F|F",
#     "F->( E )|id|ε"
# ]
# YA PASO ESTA GRAMATICA
# grammar = [
#     "E->E + T|T",
#     "T->T * F|F",
#     "F->( E )|id"
# ]
# YA PASO ESTA GRAMATICA
# grammar = [
#     "E->E + E",
#     "E->E * E",
#     "E->0|1|2|3|4|5|6|7|8|9",
#     "E->A|E",
#     "A->A A",
#     "A->( A )",
#     "A->a",
# ]
# YA PASO ESTA GRAMATICA
# grammar = [
#     "S->NP VP",
#     "VP->VP PP",
#     "VP->V NP",
#     "VP->cooks|drinks|eats|cuts",
#     "PP->P NP",
#     "NP->Det N",
#     "NP->he|she",
#     "V->cooks|drinks|eats|cuts",
#     "P->in|width",
#     "N->cat|dog",
#     "N->beer|cake|juice|meat|soup",
#     "N->fork,|knife|oven|spoon",
#     "Det->a|the"
# ]
# grammar = [
#         "S->A B|VP A|C P A",
#         "A->a A|P B",
#         "A->ε",
#         "B->b B A",
#         "B->ε",
#         "VP->c",
#         "C->d P",
#         "C->P e|e",
#         "P->ε"
#     ]
# YA PASO ESTA GRAMATICA
# grammar = [
#     "S->a S|A|C",
#     "A->a",
#     "B->a a",
#     "C->a C b"
# ]
# YA PASO ESTA GRAMATICA
grammar = [
    "S->A B",
    "A->a A A|ε",
    "B->b B B|ε"
]
# YA PASO ESTA GRAMATICA
# grammar = [
#     "S->A S A S A|a B|B|S|ε",
#     "A->B|S|ε",
#     "B->b|A|B"
# ]
# YA PASO
# grammar = [
#     "S->A S A S A|c|ε",
#     "A->b|ε"
# ]
# YA PASO
# grammar = [
#     "S->a S|A|C",
#     "A->a",
#     "B->a a",
#     "C->a C b"
# ]
# YA PASO
# grammar = [
# "S->A|ε|Z|b S|Np Detr|a TU",
# "A->B E|z B|ε|w|Cas",
# "E->a|ε",
# "Cas->a Cas b|b S",
# "Detr->0",
# "TU->O TU O TU|B A S|u Cas",
# "O->TU O TU"
# ]
# YA PASO ESTA GRAMATICA
# grammar = [
#     "E->T X|F Y|L Z|id",
#     "X->P W|P T",
#     "T->F Y|L Z|id",
#     "Y->M V|M F",
#     "F->L Z|id",
#     "Z->E R",
#     "W->T X",
#     "V->F Y",
#     "L->(",
#     "R->)",
#     "P->+",
#     "M->*"
# ]
# YA PASO LA GRAMATICA
# grammar = [
#     "E->T X",
#     "X->+ T X|e",
#     "T->F Y",
#     "Y->* F Y|e",
#     "F->( E )|id"
# ]
# grammar = cargar_gramatica("./NuevaImplementacion/prueba1.txt")
# grammar = cargar_gramatica("./NuevaImplementacion/prueba2.txt")
print(grammar)
gramatica, no_terminales, terminales = arreglar_gramatica(grammar)

print("Gramatica arreglada: "+str(gramatica))
print("No terminales:"+str(no_terminales))
print("Terminales:"+str(terminales))
print("\n___________________________________________________________________________________________________\n")
gramatica = eliminar_producciones_epsilon(gramatica)
print("Gramatica sin producciones epsilon: "+str(gramatica))
print("\n___________________________________________________________________________________________________\n")
gramatica, no_terminales = eliminar_recursividad(gramatica, no_terminales)
print("Gramatica sin recursividad:"+str(gramatica))
print("No terminales:"+str(no_terminales))
gramatica = eliminar_producciones_epsilon(gramatica)
print("\n___________________________________________________________________________________________________\n")
print("Gramatica sin producciones epsilon: "+str(gramatica))
print("\n___________________________________________________________________________________________________\n")
gramatica = remover_producciones_unitarias(gramatica)
print("Gramatica sin producciones unitarias: "+str(gramatica))
print("\n___________________________________________________________________________________________________\n")

gramatica = remover_producciones_inutiles(gramatica, no_terminales, terminales)
print("Gramatica sin producciones inutiles: "+str(gramatica))
print("\n___________________________________________________________________________________________________\n")
gramatica = conversion_chomsky(gramatica=gramatica, terminales=terminales)
print("Gramatica en forma normal de chomsky: "+str(gramatica))
gramatica = otro_formato(gramatica)

