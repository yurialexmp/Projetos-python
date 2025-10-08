from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções
[0] Pedra
[1] Papel
[2] tesoura''')
jogador=int(input('Qual a sua Jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=-' * 10)
print('o computador escolheu {}'.format(itens[computador]))
print('o jogador escolheu {}'.format(itens[jogador]))
print('-=-'* 10)

if computador == 0: # cpu escolhe pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: # cpu escolhe papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        PRINT('JOGADOR VENCE')
    else:
      print('JOGADA INVALIDA')

elif computador == 2: # cpu escolhe tesoura
    if jogador == 0:
       print('JOGADOR VENCE')
    elif jogador == 1:
       print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')










