# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print(f'{ano} É um ano bissexto!')
else:
    print(f'{ano} NÃO é um ano bissexto!')
