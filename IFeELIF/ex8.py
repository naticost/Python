"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida """

H = float(input("qual sua altura? "))
P = float(input("qual seu peso ? "))
IMC = P / (H **2) #ou pode ser H*H

if IMC < 18.5:
  print("ABAIXO DO PESO")
elif IMC>=18.5 and IMC<25:
  print("PESO IDEAL")
elif IMC>= 25 and IMC<30: #18.5 <= IMC < 25 pode ser assim
  print("SOBREPESO")
elif IMC>=30 and IMC<40:
  print("OBESIDADE")
else:
  print("OBESIDADE MÓRBIDA")

print("seu IMC é: {:.1f}".format(IMC))