# Uma das linhas do script é executado, nunca ambos

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('---FIM---')

tempo = int(input('Quantos anos tem o seu carro? '))
print('Carro Novo' if tempo <= 3 else 'Carro Velho')
print('---FIM---')
