"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo"""

nome = str(input('Qual seu nome? '))
ano = int(input("Qual seu ano de nascimento? "))
alistamento =(2022 - ano )
if alistamento < 18:
  print('ainda vai se alistar ao serviço militar')
elif alistamento == 18:
  print('é a hora exata de se alistar')
else:
  print("já passou do tempo do alistamento")

tempo = (alistamento - 18)
if tempo>0:
  print('Já se passaram {} anos do prazo'.format(tempo))
else:
  print("Ainda faltam {} anos para você se alistar".format(tempo))