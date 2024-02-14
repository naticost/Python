"""Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."""
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

from random import randint
itens= ('Pedra','Papel','Tesoura')
computador = randint(0,2)
escolha = int(input("Qual sua jogada ? "))

print('='*22)
print('o computador jogou {}'.format(itens[computador]))
print('o jogador jogou {}'.format(itens[escolha]))
print('='*22)

if computador == 0: #computador jogou PEDRA
   if escolha == 0:
     print('EMPATE')
   elif escolha == 1:
     print('JOGADOR VENCE')
   elif escolha ==2:
     print('COMPUTADOR VENCE')
   else:
    print('jogador inválida')

elif computador == 1: #computador jogou PAPEL
   if escolha == 0:
     print("COMPUTADOR VENCE")
   elif escolha == 1:
     print('EMPATE')
   elif escolha ==2:
     print('jogador vence')
   else:
    print('jogador inválida')

elif computador == 2: #computador jogou TESOURA
   if escolha == 0:
     print("jogador vence")
   elif escolha == 1:
     print('computador vence')
   elif escolha ==2:
     print("empate")
   else:
    print('jogador inválida')