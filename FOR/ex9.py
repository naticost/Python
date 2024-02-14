"""crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores."""
cont = 0
m = 0
for c in range (1, 8):
  i = int(input('digite a {} idade: '.format(c)))
  if(i>=18):
    cont+=1
  else:
    m+=1
print("O número de pessoas com maior idade é {}, e menor idade {}".format(cont, m))
