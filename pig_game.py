#Author: Gabriela Dellamora Paim

#Version: 13.02.22
import numpy as np
import functions as fun
from time import sleep as sleep
import os
import platform

'''Menu'''


#arrumar print de mensagem vc perdeu (apagando antes de poder ler)

sis_op=platform.system()
if sis_op == 'Windows': 
    comando = 'cls'
else:
    comando = 'clear'

os.system(comando)
player= None
computer = None
pp = None
cp = None

language= fun.define_language()
if language == 'English':
    texto_explicacao = '''
     ___________________________________________________________________________________________________________________
    |[Gameplay:]                                                                                                        |
    |   Each turn, a player repeatedly rolls a dice until eiter a 1 is rolled or the player decides to hold:            |
    |   - If the player rolls a 1, they score nothing from their turn and it becomes the next player's turn;            |
    |   - If the player rolls any number, it is added to their turn total and the player's turn continues;              |
    |   - If a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn. |
    |                                                                                                                   |
    |[How to win:]                                                                                                      |
    |   The first player to score 100 or more points win.                                                               |
    |___________________________________________________________________________________________________________________|
    '''
    texto_player_name='How you want to be called, player? '
    texto_hold = 'Wanna pass your turn? (Y/N)'
    text_error_hold= 'Answer not registred. Please, rewrite yout decision (Y/N) '
    
    texto_pass = 'decided to pass their turn.'
    text_not_pass='decided to play one more turn.'
    text_zero_points = ' lost all their points..'
    text_dice = 'The dice rolled: ' 
    text_computer='Computer'   
    text_winner = 'The winner for this match is: '
    text_round = '\'s round]'
    text_player_points='player points '
    text_placar_comp='''
-----------------------------
 final points for this turn!!  
 player {computer}:  {cp}
-----------------------------
          '''
          
    text_placar_player='''
-----------------------------
 final points for this turn!!  
 player {player}:  {pp}
-----------------------------
          ''' 
    text_pass_round= "Next player's round: "
    

    
    
if  language == 'Portugues':
    texto_explicacao = '''
     ________________________________________________________________________________________________________________________________
    |[Gameplay:]                                                                                                                     |
    |   Em cada rodada um jogador repetidamente rola um dado até que resulte em um valor 1 ou o jogador decide 'segurar':            |
    |   - Se o dado resultar em 1, o jogador não mantém nenhuma pontuação de sua rodada e o turno do próximo jogador começa.         |
    |   - Se o dado resultar em qualquer número, é adicionado o valor à pontuação total do turno e o jogador atual continua jogando; |
    |   - Se o jogador decide 'Segurar', a pontuação total do turno é adicionado ao seu score e o turno do próximo jogador começa.   |
    |                                                                                                                                |
    |[Como vencer:]                                                                                                                  |
    |   O primeiro jogador a pontuar 100 pontos ou mais vence.                                                                       |
    |________________________________________________________________________________________________________________________________|
    '''
    texto_player_name = 'Como deseja se chamar, jogador? '
    texto_hold= 'Deseja passar a vez? (S/N) '
    text_zero_points=' perdeu todos seus pontos! Que pena :)'
    texto_pass = ' decidiu passar sua vez.'
    text_not_pass = ' decidiu jogar mais uma vez.'
    text_dice = 'O dado rolou o valor: '
    text_computer='Computador'
    text_winner = 'O vencedor desta rodada é: '
    text_value_one = 'Seus pontos foram zerados! '
    text_error_hold= 'Resposta não registrada, por favor, reinserir decisão (S/N) '
    text_player_points= 'Pontos do jogador '
    text_placar_comp='''
-----------------------------
 Pontos finais desta rodada!  
 JOGADOR {computer}:  {cp}
-----------------------------
          '''(computer=computer, cp=cp)
    text_placar_player='''
-----------------------------
 Pontos finais desta rodada!  
 JOGADOR {player}:  {pp}
-----------------------------
          '''
    text_pass_round= 'Vez do jogador: '
print(texto_explicacao)


'''Jogo'''
sleep(4)
player=str(input(texto_player_name))
computer=text_computer
pp = 0
cp = 0

while cp < 100 or pp < 100:
    
    hold = False 
    while hold == False:
        add_point = (np.random.randint(low=1,high=7))
        print(text_dice, add_point)
        sleep(1)
        if add_point == 1:
            pp = 0
            print(player, text_zero_points)
            sleep(3)
            break
        else:
            pp += add_point
            print()
            print(player,': ', pp)
            
            hold = fun.hold_decision(txt_hold=texto_hold, txt_hold_ERROR=text_error_hold)
            if hold == False:
                print(player, text_not_pass)
                sleep(3)
            else:
                print(player, texto_pass)
                sleep(1)    
    os.system(comando)
    print(text_placar_player)
        
    print(text_pass_round, computer)  


    hold = False
    while hold == False:
        add_point = (np.random.randint(low=1,high=7))
        print(text_dice, add_point)
        if add_point == 1:
            cp = 0
            
            print(computer, text_zero_points)
            sleep(3)
            print()
            break
        
        else:
            cp += add_point
            print()
            print(computer,': ', cp)
            
            hold = fun.hold_computer(txt_hold=texto_hold, txt_hold_ERROR=text_error_hold)
            if hold == False:
                print(computer, text_not_pass)
                sleep(3)
            else:
                print(computer, texto_pass)
                sleep(1)
            
    os.system(comando)
    print(text_placar_comp)
    
    print(text_pass_round, player)  
    


'''ending game'''        
if pp >= 100:
    print(text_winner, computer)
elif cp >= 100:
    print(text_winner, computer)
    