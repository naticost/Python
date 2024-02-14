""" veja se os lados formados formam um triângulo, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes"""

r1 = float(input("primeiro segmento:"))
r2 = float(input("segundo segmento:"))
r3 = float(input("terceiro segmento:"))
if r1< r2+ r3 and r2< r1 + r3 and r3< r1 + r2:
  print("podem formar um triângulo ", end='')
  if r1 ==r2==r3:
    print("equilátero")
  elif r1 != r2 != r3 != r1:
    print("escaleno")
  else: 
    print('isósceles')
else:
  print("Não podem formar triângulo")