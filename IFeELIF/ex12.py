"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros"""

preço = float(input("valor das compras: "))
print( '''forma de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opção = int(input('qual é a opção? '))
if opção==1:
  total= preço-(preço*10/100)
  
elif opção ==2:
  total = preço - (preço * 5 /100)

elif opção == 3:
  total= preço
  parcela = total /2
  print('sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))

elif opção ==4:
  total = preço + (preço *20/100)
  totparc= int (input('quantas parcelas ? '))
  parcela = total / totparc
  print('sua compra será parcelada em {} x de R$ {:.2f}'.format(totparc,parcela))

else:
  total = 0
  print('opção inválida')
print('sua compra de R$ {:.2f} vai custar R${:.2f} no final'.format(preço,total))

