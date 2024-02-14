#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo=str(input('Qual seu sexo? [F/M]')).upper()
while sexo != "F" and sexo != "M":
    print("sexo não reconhecido, digite novamente")
    sexo=str(input('Qual seu sexo? [F/M]')).upper()
print("Sexo válido:", sexo)
