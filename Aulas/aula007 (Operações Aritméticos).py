# Operadores Aritméticos:
# '+' - Adição
# '-' - Subtração
# '*' - Multiplicação
# '/' - Divisão
# '**' - Potência - 'pow(base, expoente)' = pow(4, 3) == 64
# 'n**(1/r)' - Em que n = radicando e r = raiz;
# Exemplo: Raiz quadrada de 25 = 25**(1/2)
# '//' - Divisão Inteira
# '%' - Resto da divisão
# Utiliza dois símbolos de igual para cálculos de aritmética
print(5 + 2, 5 - 2, 5 * 2, 5 / 2, 5 ** 2, 5 // 2, 5 % 2)
5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2
5 % 2 == 1

# Ordem de Precedência:
# 1º: '()' - Parênteses
# 2º: '**' - Potências
# 3º: '**', '/', '//', '%' - Multiplicação, Divisão, Divisão Inteira e Resto da divisão
# 4º: '+' e '-' - Adição e Subtração

# Exemplos:
print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)

# Utilizando strings:
print('Oi' + 'Olá') == 'OiOlá'
print('Oi' * 5) == 'OiOiOiOiOi'
nome = str(input('Qual o seu nome: '))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

# Utilizando números:
n1 = int(input('Um valor: '))
n2 = int(input('Segundo valor: '))
print('A soma entre os números é {}'.format(n1 + n2))

n1 = int(input('Um valor: '))
n2 = int(input('Segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('Soma é {},\n produto é {}, \n divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {}, potência é {}'.format(di, p))

# Syntax:
# '\n' - Quebra um linha no comando
# "end=''" Não quebra um linha de um comando para outro
