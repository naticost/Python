"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER"""
from datetime import date
atual = date.today().year

ano = int (input('em qual ano você nasceu ? '))
idade = (atual - ano)
if idade<= 9 :
  print('Sua categoria é mirim')

elif idade > 9 and idade <=14:
  print("sua categoria é infantil")

elif idade > 14 and idade<= 19:
  print("sua categoria é júnior")

elif idade > 19 and idade<=25:
  print("sua categoria é sênior")

else:
  print("sua categoria é master")
