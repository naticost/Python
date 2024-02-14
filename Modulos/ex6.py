#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('digite um nome: '))
n2 = str (input('digite um nome: '))
n3 = str (input('digite um nome: '))
n4 = str (input('digite um nome: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('a ordem da apresentação será')
print(lista)