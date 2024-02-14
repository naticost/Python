n1 = int(input("digite um número: "))
n2 = int(input("digite um número: "))

opção = 0

while opção != 5:

  print('''Escolha uma das opções:

  [ 1 ] somar

  [ 2 ] multiplicar

  [ 3 ] maior

  [ 4 ] novos números

  [ 5 ] sair do programa''')
  opção = int(input("qual é a sua opção? "))

  if opção == 1:
    soma = n1 + n2
    print('a soma é {}'. format(soma))


  elif opção == 2:
    produto = n1 * n2
    print('o resultado é {}'.format(produto))


  elif opção == 3:
    if n1>n2:
      maior = n1
    else:
      maior = n2
    print('o número maior é {}'.format(maior))

  elif opção == 4:
    print("Informe o número novamente")

    n1 = int(input("digite um número: "))
    n2 = int(input("digite um número: "))



  elif opção == 5:
    print("finalizando...")
  else:
    print("opção inválida. Tente novamente")

print ('fim do programa! Volte sempre! ')