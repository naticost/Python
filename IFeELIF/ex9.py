H = float(input("qual sua altura? "))
P = float(input("qual seu peso ? "))
IMC = P / (H **2) #ou pode ser H*H
print("seu IMC é: {:.1f}".format(IMC))

if IMC < 18.5:
  print("ABAIXO DO PESO")
elif 18.5 <= IMC <25:
  print("PESO IDEAL")
elif 18.5 <= IMC < 25:
  print("SOBREPESO")
elif 30 <= IMC <40:
  print("OBESIDADE")
elif IMC >= 40:
  print("OBESIDADE MÓRBIDA")