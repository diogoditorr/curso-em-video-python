# Calcula quantos dolares você pode comprar com determinada quantidade de dinheiro

dinheiro = float(input('Quantos reais você tem em sua carteira?: '))
dolar = int(dinheiro//4.07)
print('Você pode comprar: {} dólares (${})'.format(dolar, dolar))