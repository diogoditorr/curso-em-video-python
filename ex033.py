# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Selecione o primeiro número: '))
b = int(input('Selecione o segundo número: '))
c = int(input('Selecione o terceiro número: '))
lista = [a, b, c]

print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')

# Outra forma: colocando a lista em ordem crescente com sorted('lista')

a = int(input('Selecione o primeiro número: '))
b = int(input('Selecione o segundo número: '))
c = int(input('Selecione o terceiro número: '))

lista = [a, b, c]
lista_ordenada = sorted(lista)

print(f'Menor número é {lista_ordenada[0]}')
print(f'Maior número é {lista_ordenada[2]}')
