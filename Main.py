''' 
MAIN File
'''
from FileReader import *

t = createTouringMultiTapeFromFile("./turing.yaml")
# create_turing_machine_graph("./turing4.yaml")
# t = createTouringFromFile("./turing4.yaml")

t.evaluate_strings()
