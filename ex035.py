# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
a = int(input('Digite o lado 1 do triângulo: '))
b = int(input('Digite o lado 2 do triângulo: '))
c = int(input('Digite o lado 3 do triângulo: '))

if a < b + c and b < a + c and c < a + b:
    print('O triângulo com lados {}, {} e {} pode existir.'.format(a, b, c))
else:
    print('É impossível formar um triângulo com essas medidas...')