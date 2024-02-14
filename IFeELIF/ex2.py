"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""
num=int(input('digite um número inteiro: '))
print('''escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')

opção = int(input('sua opção: '))
if opção ==1:
  print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
  print('{} convetido para octal é igual a {}'.format(num, oct(num)[2:]))
  
elif opção == 3:
  print('{} convertido em hexadecimal {}'.format(num, hex(num)[2:]))
  #quando escolher essa opção irá aparecer na frente um 0X- significa hexadecimal em python,que podemos tirar essa string
else:
  print('opção inválida. Tente novamente.')