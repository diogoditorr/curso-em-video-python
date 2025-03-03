# Faça um progrmaa que leia um número de 0 a 9999 e mostra na tela cada um
# dos dígitos separados.

# Ex:
# Digite um número: 1834

# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

number = int(input("Digite um número: "))
if len(number.__str__()) > 4:
    print("Escolha maior que 4 digítos. Desligando...")
    exit()

number = '000' + number.__str__()
print(f'Unidade: {number[-1]}\n'
      f'Dezena: {number[-2]}\n'
      f'Centena: {number[-3]}\n'
      f'Milhar: {number[-4]}\n')