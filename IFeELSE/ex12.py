#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal=float(input('digite seu salário: R$ '))
if sal<=1250:
  print('seu novo salário é com 15% a mais: R$ {:.2f}'.format(sal+(sal*15/100)))
else:
  print('seu novo salário é: R$ {:.2f}'.format(sal+(sal*10/100)))