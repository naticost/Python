#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente. 
n = str(input('digite seu nome compelto: ')).strip()
nome =n.split()
print('seu primeiro nome é: {}'. format(nome[0]))
print('seu ultimo nome é: {}'.format(nome[len(nome)-1]))