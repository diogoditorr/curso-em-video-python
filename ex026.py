# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes Aparece a letra 'a';
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez

phrase = str(input('Digite uma frase: ')).upper().strip()
print(f'Possui letras "a": {phrase.count("A")}')
print(f'A primeira letra "a" foi encontrado: {(phrase.find("A") + 1)}º')
print(f'A última letra "a" foi encontrado: {(phrase.rfind ("A") + 1)}º')