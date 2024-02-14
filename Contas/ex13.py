#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la;sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
L = float(input('digite o valor da largura: '))
H = float(input('digite i valor da altura: '))
A = L*H
T = A/2
print('a quantidade de tintas usada na área do quadrado é: {} litros'.format(T))