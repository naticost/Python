"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo"""
from datetime import date
atual = date.today(). year
nasc = int(input('ano de nascimento: '))
idade = (atual - nasc)
print ('quem nasceu em {} tem {} anos em {}. '.format(nasc, idade, atual))
if idade == 18:
  print('você tem que se alistar imediamente')
elif idade < 18:
  saldo = 18 - idade
  print(' ainda faltam {} anos para o alistamento'.format(saldo))
  ano = atual + saldo
  print('seu alistamento será em {}'.format(ano))
elif idade > 18:
  saldo = idade - 18
  print('você já deveria ter se alistado há {} anos'.format(saldo))
  ano = atual - saldo
  print('seu alistamento foi {}'.format(ano))