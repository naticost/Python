"""faça desafio da tabuada de um número que o usuário escolhe, utilizando for"""
n = int(input('digite um valor: '))
for c in range (1, 11):
  """x = n*c"""
  print('{} x {:2} = {}'.format(n, c, n*c))