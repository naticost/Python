# onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint (0, 10)
print("sou seu computador... acabei de pensar em um número entre 0 e 10 ")
print("será que você consegue adivinhar qual foi?")
acertou = False
palpite = 0
while not acertou:
  jogador = int (input("qual é o seu palpite?"))
  palpite += 1
  if jogador == computador:
    acertou = True
  else:
    if jogador<computador:
      print("mais...tente mais uma vez")
    elif jogador>computador:
      print("menos..tente mais uma vez")
print('certou {} tentativas'.format(palpite))