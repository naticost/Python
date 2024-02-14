#leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase =str(input('digite uma frase: ')).upper() .strip
print('quantas vezes tem a letra A:{}'.format(frase.count('A')))
print('posição da primeira letra A {}'.format(frase.find('A')+1))
print('a ultima posição que a letra A apareceu foi {}'.format(frase.rfind('A')+1))