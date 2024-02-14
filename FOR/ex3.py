
"""faça um programa que mostre  na tela uma contagem regressiva para o estouro de fogos de artifício , indo de 10 até 0, com uma pausa de 1 segundo entre eles"""
for c in range(10, 0, -1):
  print(c)
print("FOGOS")

s=0
for c in range (0,3):
  n = int(input('digite um valor: '))
  s+=n
print(s)