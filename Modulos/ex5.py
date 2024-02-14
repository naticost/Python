#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
N1= str(input('digite um nome: '))
N2 = str(input('digite um nome: '))
N3 = str(input('digite um nome: '))
N4 = str(input('digite um nome:'))
Lista = [N1, N2, N3, N4]
escolhido = choice(Lista)
print('o escolhido é {}'.format(escolhido))
