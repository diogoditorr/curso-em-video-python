# Cálculo da hipotenusa de um triangulo retângulo

from math import hypot
c_a = float(input('Lado adjacente: '))
c_o = float(input('Lado oposto: '))

h = hypot(c_o, c_a)
print(f'Triângulo retângulo de lados {c_o} e {c_a} tem seu comprimento da hipotenusa: {h:.1f}')
