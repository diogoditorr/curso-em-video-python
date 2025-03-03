# Mostra tipo de variável e várias informções sobre ele

p = input('Digite qualquer coisa: ')
print('Tipo de viariável: {}'.format(type(p)))
print('É um número ou/com letra?: {}'.format(p.isalnum()))
print('É número?: {}'.format(p.isnumeric()))
print('É letra?: {}'.format(p.isalpha()))
print('Possue letras e número em códigos?: {}'.format(p.isascii())) #Exemple: U+000-U+007f
print('É decimal?: {}'.format(p.isdecimal()))
print('É uma variável dígito?: {}'.format(p.isdigit()))
print('É identificador de Python válido?: {}'.format(p.isidentifier()))
print('Todas as letras estão minúsculas?: {}'.format(p.islower()))
print('É possível ser printado na tela?: {}'.format(p.isprintable()))
print('Tem espaço na string?: {}'.format(p.isspace()))
print('É um título?: {}'.format(p.istitle()))
# Each first character is Upper and the others one lower
print('Todas as letras são maiúsculas?: {}'.format(p.isupper()))

exit()
# First character in each word is
# uppercase and remaining lowercases
s = 'Geeks For Geeks'
print(s.istitle())

# First character in first
# word is lowercase
s = 'geeks For Geeks'
print(s.istitle())

# Third word has uppercase
# characters at middle
s = 'Geeks For GEEKs'
print(s.istitle())

s = '6041 Is My Number'
print(s.istitle())

# word has uppercase
# characters at middle
s = 'GEEKS'
print(s.istitle())

