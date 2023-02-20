import numpy as np
from time import sleep as sleep


def hold_decision(txt_hold:str, txt_hold_ERROR:str):
    t_hold = (input(txt_hold))
    if t_hold == 'N' or t_hold == 'n':
        hold = False
        return hold
    if t_hold == 'Y' or t_hold == 'S' or t_hold == 'y' or t_hold == 's':
        hold = True
        return hold
    else:
        while t_hold != 'Y' or t_hold != 'y' or t_hold != 's' or t_hold != 's' or t_hold != 'N' or t_hold != 'n':
            print(txt_hold_ERROR)
            return hold_decision(txt_hold=txt_hold, txt_hold_ERROR=txt_hold_ERROR)
        
def hold_computer(txt_hold:str, txt_hold_ERROR:str):
    sleep(3)
    rand= np.random.randint(low=0,high=2)
    if rand == 0: 
        hold = False
    else:
        hold = True
    return hold

def define_language():
    language= str(input('Select your language. write \'E, or English\' for ENGLISH  | Selecione seu idioma. Escreva \'P, ou Portugues\' para Português: '))
    if language == 'P' or language == 'p' or language == 'PORTUGUES' or language == 'portugues' or language == 'Portugues':
        return 'Portugues'
    if language == 'E' or language == 'e' or language == 'ENGLISH' or language == 'english' or language == 'English':
        return 'English'
    else:
        print('Language not identified.')
        print('')
        return define_language()