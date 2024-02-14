#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
nu=int(input("digite um número "))
n = str(nu)
print('analisando o número {}'.format(nu))
print('Unidade:{}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))