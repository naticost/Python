# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
L = float(input('digite o valor da largura: '))
D = L - ( L*5/100 )
print('o valor do produto R$ {} com 5% de desconto fica R$ {} '.format(L,D))