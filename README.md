# PIG-GAME

Author: Gabriela Dellamora Paim
Version: 1.0
Date: 2023/02/14
Um projeto simples para treinar lógica de programação em python.
Para este projeto, foram usadas as bibiotecas:
 - Numpy
 - Time
 - Os
 - Platform

 Explicação do código:
 O jogo todo é formado dentro de um laço _while_, com controle de fluxos.
 A decisão da linguagem é feita por meio de controle de fluxos, ou seja: caso P, português (e todas variáveis utilizadas no código serão definidas), caso E, inglês, e igualmente, todas variáveis serão definidas nesse momento. A partir desta decisão, todos os valores de string mutáveis serão definidos.

 Uma definição importante para a funcionalidade do código é o arquivo com suas funções, o functions.py o qual possui 3 funções:
 - hold_decision()
    serve para perguntar ao usuário se ele decide passar a vez, retornando um valor booleano que mantém o usuário no laço while atual;
 - hold_computer()
    serve para deifinir a decisão do computador, utilizando funções da biblioteca _numpy_ (random.randint) para retornar valores booleanos, sendo 50/50 chances de decidir passar a vez ou não.
 - define_language()
    serve para manter o código main organizado e separar a lógica por detrás da definição do idioma do jogo.


# Informações importantes:
## Sistemas operacionais suportados:
    - Windows
    - Linux
### *ATENÇÃO:*
### *Para rodar este projeto é necessário ter instalado no computador o interpretador python3*


# Como rodar o jogo no meu computador Windows?
 1- abra o terminal do seu computador utilizando a tecla windows e escrevendo 'cmd' na barra de pesquisas. 
 
 2 -  abra a pasta onde os arquivos do jogo foram armazenados por meio do comando cd;.
 
    Exemplo: 'cd Downloads/Jogos/PIG-GAME'
 
 3 - Após abrir a pasta onde os arquivos estão armazenados, utilize o comando 'dir' para checar se a pasta possui dois arquivos os seguintes arquivos;
 
    - functions.py
    - pig_game.py
    - README.md

4 - Para finalmente poder jogar o pig game, basta utilizar o comando 'python pig_game.py'.

# Como rodar o jogo no meu computador Linux?

 1- acesse o terminal do seu computador utilizando o comando ctrl+T;
 
 2 -  abra a pasta onde os arquivos do jogo foram armazenados por meio do comando cd;
    
    Exemplo: 'cd Downloads/Jogos/PIG-GAME'
 
 3 - Após abrir a pasta onde os arquivos estão armazenados, utilize o comando 'ls' para checar se a pasta possui dois arquivos os seguintes arquivos;
 
    - functions.py
    - pig_game.py
    - README.md

4 - Para finalmente poder jogar o pig game, basta utilizar o comando 'python pig_game.py'.