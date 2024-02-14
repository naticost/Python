#tente adivinhar 
from random import randint
from time import sleep
computador = randint(0,5) #faz o computador pensar
print('-=-'*30)
print('vou pensar em um número entre 0 a 5. Tente adivinhar ...')
jogador = int(input('Em que número eu pensei ?')) #jogador tenta adivinhar
sleep(2) #pausa de 2 segundos
if jogador == computador:
  print('Parabéns!Você conseguiu me vencer!')
else:
  print('Ganhei! Eu pensei no número {} e não no {}'.format(computador,jogador))