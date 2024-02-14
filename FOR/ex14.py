"""Desenvolva um programa que leia seis números inteiros e monstre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o"""
soma = 0
cont = 0
for c in range (1, 7):
  num = int(input('digite o {} valor: '.format(c)))
  if num %2 ==0:
    soma+=num
    cont+=1
print('você informou {} números pares e soma foi {}'.format(cont, soma))