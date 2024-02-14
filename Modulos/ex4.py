#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
import math
an = float(input('digite o valor do ângulo:'))
seno = math.sin(math.radians(an))
print('o ângulo {} tem o seno {:.2f}'.format(an,seno))
cosseno = math.cos(math.radians(an))
print('o ângulo {} tem o cosseno{:.2f}'.format(an,cosseno))
tangente = math.tan(math.radians(an))
print('o ângulo {} tem a tangente {:.2f}'.format(an,tangente))