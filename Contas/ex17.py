#pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
K=float(input('quantos Km você percorreu?'))
D = int(input('quantos dias você ficou com o carro? '))
Vk= K*0.15
VD = D*60
print('o valor total a pagar é {} + {} = {}  '.format(Vk,VD,Vk+VD))
