"""Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome"""
a=str(input('digite um nome: '))
print('nome no minusculo[]'.format(a.upper()))
print('nome no maiusculo[]'.format(a.lower()))
print('nome contado sem espaços:{}'.format(len(a.strip())))
print('nome tem {} letras'.format(a.find(" ")))