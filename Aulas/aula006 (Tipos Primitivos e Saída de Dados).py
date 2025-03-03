n = input('Digite algo: ')
print('É um número?', n.isnumeric())
print('É uma letra?', n.isalpha())
print('É uma letra ou/com número?', n.isalnum())
# There are a lot of variable.is[IDENTIFY]

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
# print('A soma entre', n1, 'e', n2, 'vale:', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
print('A soma entre {0} e {2} vale {1}'.format(n1, n2, s))
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))
print(f'A soma entre {n1} e {n2} vale {s}')

n = float(input('Digite um valor: '))
print(n)

n = str(input('Digite um valor string: '))
print(n)
print(type(n))

n = bool(input('Digite um valor (boolean): '))
print(n)
# Show false if there's no value in the N, and true if there's


