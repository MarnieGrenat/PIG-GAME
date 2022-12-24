#Author: Gabriela Dellamora Paim

#Version: 16.12.22
import numpy as np

language= str(input('Select your language. write \'E, or English\' for ENGLISH  | Selecione seu idioma. Escreva \'P, ou Portugues\' para Português: '))

if language == 'E' or language == 'e' or language == 'ENGLISH' or language == 'english' or language == 'English':
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
    texto_hold = 'Wanna hold? (Y/N)'
    text_dice = 'The dice rolled: ' 
    text_computer='Computer'   
    text_winner = 'The winner for this match is: '
    text_round = '\'s round]'
    text_value_one = 'zero point!'
    
    
if language == 'P' or language == 'p' or language == 'PORTUGUES' or language == 'portugues' or language == 'Portugues':
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
    text_hold= 'Deseja segurar? (S/N)'
    text_dice = 'O dado rolou o valor: '
    text_computer='Computador'
    text_winner = 'O vencedor desta rodada é: '
    text_round = '\'s round]'    ############
    text_value_one = 'Seus pontos foram zerados!'

else:
    print('Language not identified. Please, restart the game.')
    

print(texto_explicacao)
player=str(input(texto_player_name))
computer=text_computer
pp = 0
cp = 0

hold = False
while hold is False:
    pass