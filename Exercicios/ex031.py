# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.

distance = int(input('Qual a distância da sua viagem em Km? '))

if distance <= 200:
    price = 0.5 * distance
else:
    price = 0.45 * distance
print(f'Sua passagem irá custar: R$ {price}')
