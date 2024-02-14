#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.RELEMBRAR
pre = float(input('digite o valor do produto: R$ '))
#novo = pre - (pre * 5 / 100)
print('o valor do produto com 5% de desconto é: R$ {:.2f}'.format(pre - (pre * 5 / 100)))