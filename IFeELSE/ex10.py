# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('digite um número: '))
b = int(input('digite um número: '))
c = int(input('digite um número: '))
#verificando quem é menor
menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c
#verificando quem é maior
maior = a
if b > a and b> c:
  maior = b
if c > a and c > b:
  maior = c

print('o menor valor é {}'.format(menor))
print(' o maior é {}'.format(maior))
#print('o maior valor é {}'.format(maior))