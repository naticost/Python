#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
CA = float (input('digite um valor: '))
Co = float(input('digite um valor: '))
H = math.hypot(Co,CA)
print('a hipotenusa é: {:.2f}.'.format(H))
#H = (Co **2 + CA**2 )** (1/2)
#print('a hipotenusa é {:.2f}'.format(H))