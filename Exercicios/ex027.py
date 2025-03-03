# Faça um programa que leia o nome completo de uma pessoa, mostrando em
# seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
nome_divided = nome.split()
print(f'Nome: {nome}'
      f'\nPrimeiro: {nome_divided[0]}'
      f'\nÚltimo: {nome_divided[-1]}')
