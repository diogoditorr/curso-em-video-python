# Lê o nome de uma pessoa e diga se ela tem Silva no nome

nome = str(input('Qual seu nome completo? '))
nome = nome.upper()
print(f'Você tem "Silva" no nome?: {"SILVA" in nome}')