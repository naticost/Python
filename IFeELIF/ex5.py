"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:"
– Média abaixo de 5.0: REPROVADO

–Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO"""

A = float(input("digite sua nota: "))
B = float(input("digite sua nota: "))
med = (A+B)/2

if med < 5.0:
  print('Média abaixo de 5.0, com suas notas sua média é {:.1f}'.format(med))
  print('você está reprovado')
elif med >= 7.0:
  print('Média 7.0 ou superior, com suas notas sua média é {:.1f}'.format(med))
  print('você está aprovado')
else:
  print('Média entre 5.0 e 6.9, sua média é {:.1f}'.format(med))
  print('recuperação')