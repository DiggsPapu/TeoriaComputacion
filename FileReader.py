'''
 _____ _ _                      _         
|   __|_| |___    ___ ___ ___ _| |___ ___ 
|   __| | | -_|  |  _| -_| .'| . | -_|  _|
|__|  |_|_|___|  |_| |___|__,|___|___|_|  

Reader and parser for yaml files
'''
from TMachine import TuringMachine
from MultiTapeTMachine import *
from graphviz import Digraph
import yaml
def createTouringMultiTapeFromFile(filename) -> TuringMachine: 
    '''
    Lee un archivo yaml, retorna una maquina de touring com la 
    imformación leída en el yaml
    '''

    with open(filename, 'r') as yaml_file:
        data = yaml.load(yaml_file,Loader=yaml.FullLoader)
        inicial = data['q_states']['initial']
        final = {val for val in data['q_states']['final']}
        acc = {val for val in data['q_states']['accept']}
        blank_symbol = data['blank']
        transition_function = {}
        simulation_strings = data['simulation_strings']
        for params in data['delta']:
            lista_name = params['params']['tape_input']
            lista_name.insert(0, params['params']['initial_state'])
            transition_function[tuple(lista_name)] = (params['output']['final_state'], params['output']['tape_output'], params['output']['tape_displacement'])
        # print(transition_function)
        
        return MultiTapeTuringMachine(tapes= simulation_strings, blank_symbol= blank_symbol, initial_state = inicial, final_states=final,transition_function= transition_function, accept_states= acc)
    
def createTouringFromFile(filename) -> TuringMachine: 
    '''
    Lee un archivo yaml, retorna una maquina de touring com la 
    imformación leída en el yaml
    '''

    with open(filename, 'r') as yaml_file:
        data = yaml.load(yaml_file,Loader=yaml.FullLoader)
        inicial = data['q_states']['initial']
        final = {val for val in data['q_states']['final']}
        acc = {val for val in data['q_states']['accept']}
        blank_symbol = data['blank']
        transition_function = {}
        simulation_strings = data['simulation_strings']
        for params in data['delta']:
            transition_function[(params['params']['initial_state'], params['params']['tape_input'])] = (params['output']['final_state'], params['output']['tape_output'], params['output']['tape_displacement'])
        return TuringMachine(simulation_strings, blank_symbol, inicial, final, transition_function,acc)    
    
def create_turing_machine_graph(yaml_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    graph = Digraph(comment='Turing Machine')
    for state in data['q_states']['q_list']:
        if state in data['q_states']['final']:
            graph.node(state, shape='doublecircle')
        else:
            graph.node(state, shape='circle')
        if state in data['q_states']['initial']:
            graph.node('punto_inicial', shape='point', color="black")
            graph.edge('punto_inicial', state)
    for transition in data['delta']:
        initial_state = transition['params']['initial_state']
        final_state = transition['output']['final_state']
        tape_input = transition['params']['tape_input']
        tape_output = transition['output']['tape_output']
        tape_displacement = transition['output']['tape_displacement']
        label = f"{tape_input}/{tape_output}, {tape_displacement}"
        graph.edge(initial_state, final_state, label=label)
    graph.render(str(yaml_file)+"_graph", format='png', view=True)

# createTouringMultiTapeFromFile("./turing5.yaml")
# createTouringFromFile("./turing4.yaml")