# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
S = float(input('Qual seu salário? R$ '))
A = S + (S * 15/100)
print('o valor do seu salário de R$ {}, com 15% de aumento, seu salário passa a ser R$ {} '.format(S,A))