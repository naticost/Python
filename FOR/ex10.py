
"""crie um programa que leia a frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços"""
#strip() : retorna a string resultante após a remoção do início e do final da string s de todos os caracteres em BRANCO
# palíndromo: frase ou palavra que se pode ler, indiferentemente, da esquerda para direita ou vice-versa”: osso, Ana, radar, Renner, Roma
# função upper() retorna todos os caracteres dentro da string convertidos para maiúsculas.
#split = transfroma em lista
# [::-1] começa do 0 e vai até o final, só que de forma ao contraria, por isso -1
f = str(input('digite uma frase: ')).strip().upper()
palavras = f.split()
j = ''.join(palavras)
i = j[::-1]
print('0 inverso de {} é {}'.format(j, i))
if i == j:
  print('temos um palíndromo!')
else:
  print('a frase digitada não é um palíndromo!')