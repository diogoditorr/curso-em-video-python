# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Velocidade do carro: '))

if v > 80:
    multa = (v - 80) * 7
    print('Você foi multado por estar acima do limite de velocidade!\n')
    print(f'Sua velocidade: {v} Km/h')
    print(f'Sua multa é de: R$ {multa}.00')
else:
    print('Você está dentro do limite e por isso não foi multado.')
