''' Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: 
– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''


A = int(input('digite um número: '))
B = int(input('digite um número: '))
if A > B:
  print (" O primeiro valor {} é maior".format(A))
elif B > A:
  print (' O segundo valor {} é maior'.format(B))
else:
  print("Não existe valor maior, os dois são iguais")