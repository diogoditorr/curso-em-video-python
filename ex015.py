# Aluguel de um carro: R$60 por dia e R$0.15 por Km rodado

km = float(input('Quantos quilometros você percorreu?: '))
days = int(input('Quantos dias o carro foi alugado?: '))
total = (60 * days) + (0.15 * km)

print(f' Quilômetros rodado: {km}Km \n Dias alugado: {days} \n Total a ser pago: R${total:.2f}')