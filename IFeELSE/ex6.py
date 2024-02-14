#m programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
via = float(input('quantos km tem sua viagem? '))
if via <=200:
  print('o preço da passagem é: R${:.2f}'.format(via*0.50))
else:
  print('o preço da viagem é: R${:.2f}'.format(via*0.45))