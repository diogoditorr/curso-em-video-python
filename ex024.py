# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Qual o nome da sua cidade? '))
cidade = cidade.strip().split()
cidade[0] = cidade[0].upper()
print(f"Sua cidade começa com SANTO?: {'SANTO' in cidade[0]}")