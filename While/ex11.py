#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
r = 'S'
s = q = m = ma = me = 0
while r in 'Ss':
  n = int(input('Digite um número: '))
  s += n
  q += 1
  if q ==1:
    ma = me = n
  else:
    if n > ma:
      ma = n
    if n<me:
      me = n


  r = str(input("Quer continuar? [S/N]")).upper().strip()[0]
m = s / q
print('você digitou {} números e a média foi {} '. format(q,m))
print('O maior valor foi {} e o menor foi {}'.format (ma, me))