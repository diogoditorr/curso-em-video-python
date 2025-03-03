# Calcula o preço de um produto com 5% de desconto

valor = float(input('Qual o valor do produto?: '))
discount = float(input('Quanto você quer de desconto?: '))
new_value = float(valor - (valor*discount/100))

print
print(f' Desconto de {discount}% \n Valor do produto com desconto: R${new_value:.2f}')