# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.RELEMBRAR
sal= float(input('Diga seu salário: R$'))
print('PARABÉNS! Você recebeu um aumento de 15%, seu novo salário é: R$ {:.2f}'.format(sal+(sal*15/100)))