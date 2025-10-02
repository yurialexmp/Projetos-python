from random import randint
from time import sleep
computador=randint(0,3)
print('-=-' * 20)
print('Vou pensar em um número de 0,5. Tente adivinhar...')# número que o computador irá pensar.
print('-=-' * 20)
jogador=int(input('em que número eu pensei?:'))# número que o jogador vai pensar.
print('PROCESSANDO...')
sleep(2)
if jogador==computador:
    print('PARABÉNS VC GANHOU!!!!!')
else:
    print('Que pena ,vc perdeu hahahaha')

