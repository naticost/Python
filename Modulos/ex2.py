#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#import math
#n = float(input('digite um número: '))
#pi = math.trunc(n)
#print('a porção inteira de {} é {}'.format(n,pi)) ou fazer de um jeito mais eficiente
#detalhe: quando você digita (9,999) é lido como string, por isso digite número. (9.999)
import math
n=float(input('digite um número:'))
print('a parte de {} a porção inteira do número é: {}'.format(n,math.trunc(n)))