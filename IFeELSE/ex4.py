#programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel= float(input('Qual a velocidade do seu carro? '))
if vel >80:
  print('vocÊ foi multado:{:.2f}'.format((vel-80)*7))
else:
  print('parabêns,vocÊ não está multado')