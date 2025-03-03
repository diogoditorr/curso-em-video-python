# Mostra o seno, cosseno e tangente de um ângulo

# Primeira maneira
import math
num1 = float(input('Escreva um ângulo em graus: '))
num = num1*(math.pi)/180
print('o seno de {} é {:.2f} \n'
      'o cosseno de {} é {:.2f} \n'
      'a tangente de {} é {:.2f}'.format(num1, math.sin(num), num1, math.cos(num), num1, math.tan(num)))
exit()

# Segunda maneira
import math
a = float(input('Digite um ângulo em graus °: '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))

print('Ângulo: {}°\n Seno: {:.2f}\n Cosseno: {:.2f}\n Tangente: {:.2f}'.format(a, seno, cosseno, tangente))

# from math import cos, sin, tan, radians
# a = float(input('Digite um ângulo em graus °: '))
# seno = sin(radians(a))
# cosseno = cos(radians(a))
# tangente = tan(radians(a))
