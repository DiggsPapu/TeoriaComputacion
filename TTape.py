'''                                                                                                                           
 _______ _______ _______ _______     _______ _______ _______     _______ _______ _______ _______ _______ _______ _______    
|\     /|\     /|\     /|\     /|   |\     /|\     /|\     /|   |\     /|\     /|\     /|\     /|\     /|\     /|\     /|   
| +---+ | +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |   
| |   | | |   | | |   | | |   | |   | |   | | |   | | |   | |   | |   | | |   | | |   | | |   | | |   | | |   | | |   | |   
| |T  | | |a  | | |p  | | |e  | |   | |f  | | |o  | | |r  | |   | |m  | | |a  | | |c  | | |h  | | |i  | | |n  | | |e  | |   
| +---+ | +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |   
|/_____\|/_____\|/_____\|/_____\|   |/_____\|/_____\|/_____\|   |/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|   
                                                                                                                            
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class Tape(object):   
    blank_symbol = " " 
    def __init__(self,
                 tape_string = "",blank=" "):
        self.__tape = dict((enumerate(tape_string)))
        Tape.blank_symbol = blank
        
    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys()) 
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index+1):
            s += self.__tape[i]
        return s    
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 
