# Pega altura e largura de uma parede; calcula a área e também a quantidade de tinta para
# pintar essa parede.

# Cada litro de tinta pinta 2m^2

b = int(input('Qual a largura da parede?: '))
h = int(input('Qual a altura da parede?: '))
a = b * h
r = (a // 2) + (a % 2)

print('Área da parede: {} m \n Quantidade de tinta necessária: {} litros'.format(a, r))
