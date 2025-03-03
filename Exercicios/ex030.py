# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('Escolha um número: '))

if number % 2 > 0:
    print('O número escolhido é ÍMPAR!')
else:
    print('O número escolhido é PAR!')