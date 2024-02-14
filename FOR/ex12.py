"""desenvolva um programa que leia o nome, idade, sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1,5):
  print('---- {}ª Pessoa ----'.format(p))
  nome = str(input('Nome: ')).strip()
  idade = int(input('idade: '))
  sexo = str(input('Sexo [M/F]: ')).strip()
  somaidade+=idade
  if p == 1 and sexo in 'Mn':
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Mn' and idade > maioridadehomem:
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Ff' and idade<20:
    totmulher20+=1
media = somaidade/4
print(' a média idade do grupo é: {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print(' Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
