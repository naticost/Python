"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado"""

empr = float(input("qual o valor casa ? "))
sal = float (input('qual o valor do seu  salário? '))
ano = int(input("quantos anos você vai pagar ?"))
meses = ano/12
pm = (empr / meses ) *30/100
if pm > sal:
  print("emprestimo negado")
else:
  print('aprovado')