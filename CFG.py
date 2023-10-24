import copy
# Metodo que sirve para eliminar la recursividad
def eliminar_recursividad(gramatica:dict, no_terminales:list):
    '''
    Funcion que sirve para eliminar la recursividad de una gramatica
    
    Args:
    gramatica (dict): La gramatica original
    no_terminales (list): Los no terminales de la gramatica
    '''
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
# Metodo que sirve para calcular las parejas unarias que se obtienen con transitividad
def recursividad_parejas_unarias(gramatica:dict, parejas_unarias:list, unary_pair:tuple, no_terminales:list):
    '''
    Funcion para encontrar las parejas unitarias que se encuentra con transitividad, derivando.
    
    Args:
    gramatica (dict): Diccionario de gramaticas
    parejas_unarias (list): Listado de parejas unarias
    unary_pair (tuple): Pair de producciones
    no_terminales (list): No terminales del lenguaje
    '''
    for production in gramatica[unary_pair[1]]:
        if unary_pair[1] != production and production in no_terminales:
            new_p = (unary_pair[1],production)
            if new_p not in parejas_unarias:
                parejas_unarias.append(new_p)
                parejas_unarias = recursividad_parejas_unarias(gramatica,parejas_unarias,new_p, no_terminales)
    return parejas_unarias
# Metodo para crear las parejas unarias
def crear_parejas_unarias(gramatica:dict):
    '''
    Funcion para crear todas las parejas unarias
    
    Args:
    gramatica (dict): Diccionario de gramaticas
    '''
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
# Metodo para remover las producciones unarias
def remover_producciones_unitarias(gramatica:dict):
    '''
    Funcion para remover las producciones unitarias
    
    Args:
    gramatica (dict): Diccionario de gramaticas
    '''
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
# Metodo para que retorne el indice segun la ocurrencia de un elemento en una lista
def index_ocurrencia_elemento(lista:list, element:str, occurrence_number:int):
    '''
    Funcion para determinar el indice de la enesima ocurrencia en una lista.
    
    Args:
    lista (list): Listado a buscar
    element (str): Elemento a buscar
    occurrence_number (int): Numero de ocurrencia del elemento
    '''
    found_count = 0
    for index, item in enumerate(lista):
        if item == element:
            found_count += 1
            if found_count == occurrence_number:
                return index
    return -1
# Metodo para generar todas las posibles producciones epsilon al permutar.
def generar_producciones_epsilon(elementos:list, elemento_anulable:str, cantidad_ocurrencias:int, epsilon_productions:list = [], num_oc:int=1):
    '''
    Funcion para generar todas las posibles producciones permutando las epsilon eliminando los no terminales que derivan en epsilon
    
    Args:
    elementos (list): es una lista que representa una produccion que es epsilon
    elemento_anulable (str): Es el no terminal anulable
    cantidad_ocurrencias (int): Es la cantidad de ocurrencias de un no terminal anulable por epsilon
    epsilon_productions (list): lista con todas las producciones epsilon que se generan
    num_oc (int): Es el numero de ocurrencia a evaluar.
    '''
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
# Metodo para eliminar las producciones epsilon
def eliminar_producciones_epsilon(gramatica:dict):
    '''
    Funcion para eliminar todas las posibles producciones epsilon
    
    Args:
    gramatica (dict): Dictioario que contiene la gramatica
    '''
    anulables = []
    reglas_anulables = []
    # Identificar las producciones epsilon y remover las producciones epsilon
    for no_terminal in gramatica.keys():
        if "ε" in gramatica[no_terminal]:
            # Aniado los que son no anulables a una lista de no anulables
           anulables.append(no_terminal)
           gramatica[no_terminal].remove("ε")
            # Solo tenia una unica produccion a epsilon    
           if len(gramatica[no_terminal])==0:
               reglas_anulables.append(no_terminal)
    # Eliminar reglas borrables
    for no_terminal_eliminable in reglas_anulables:
        gramatica.pop(no_terminal_eliminable)
    # Crear una copia para no perder punteros
    gramatica_new = copy.deepcopy(gramatica)
    # Eliminar epsilons y aniadir epsilons resultantes
    for no_terminal, productions in gramatica_new.items():
        for production in productions:
            elementos = production.split(" ")
            elementos_evaluados = []
            for elemento in elementos:
                # Si es una regla eliminable
                if elemento in reglas_anulables:
                    gramatica[no_terminal].remove(production)
                    break
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
# Metodo para determinar si cierto no terminal es alcanzable
def es_alcanzable(gramatica:dict, no_terminales:list, no_terminal:str, no_terminal_inicial:str, producciones_exploradas:list): 
    '''
    Funcion para definir si un no terminal es alcanzable
    
    Args:
    gramatica (diccionario): Gramática en diccionario
    no_terminal_inicial (str): Símbolo inicial a evaluar dado que es recursivo
    no_terminal (str): No terminal que se requiere
    no_terminales (list): Lista de no terminales
    producciones_exploradas (list): producciones ya exploradas en la funcion recursiva
    '''
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
# Metodo para determinar si una produccion en especifico es util
def prod_util(no_terminal_inicial:str, gramatica:dict, reglas_utiles:dict, no_terminales:list, terminales:list, no_terminales_explorados:list):
    '''
    Metodo para determinar si una regla en especifico es util
    
    Args:
    no_terminal_inicial: Es el no terminal inicial, suele ser S.
    no_terminales: Los no termianles del lenguaje.
    gramatica: La gramatica del lenguage.
    reglas_utiles: Reglas utiles previas.
    terminales: Terminales del lenguaje.
    no_terminales_explorados: Son todos aquellos no terminales que ya han sido explorados dado que es una funcion recursiva.
    '''
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
# Metodo para remover las producciones inutiles
def remover_producciones_inutiles(gramatica:dict, no_terminales:list, terminales:list):
    '''
    Metodo para remover las producciones inutiles
    
    Args:
    gramatica (dict): Gramatica del lenguaje
    no_terminales (list): Listado de los no-terminales
    terminales (list): Listado de los terminales
    '''
    reglas_utiles = {}
    # Se supone que es el primero
    no_terminal_inicial = list(gramatica.keys())[0]
    gramatica_new = copy.deepcopy(gramatica)
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
# Metodo para convertir a chomsky
def conversion_chomsky(gramatica:dict, terminales:list):
    '''
    Metodo para convertir a chomsky una gramatica que no tenga producciones epsilon ni producciones unitarias.
    
    Args:
    gramatica (dict): Gramatica en formato de diccionario
    terminales (list): Terminales de la gramatica
    '''
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