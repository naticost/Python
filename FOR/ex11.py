"""faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""
n = int(input("digite um número: "))
tot = 0
for c in range(1, n+1):
  if n %c == 0:
    print('\033[34m', end=' ')
    tot+=1
  else:
    print('\033[m', end=' ')
  print('{}'.format(c),end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot==2:
  print(' O número digitado é primo, porque é divisível por 1 e por ele mesmo')
else:
  print('Não é primo')

