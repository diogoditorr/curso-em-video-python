from math import floor, ceil, sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz do número {} é {}'.format(num, raiz))
print('A raiz do número {} é {:.2f}'.format(num, raiz))
print('A raiz do número {} é {}'.format(num, ceil(raiz)))
print('A raiz do número {} é {}'.format(num, floor(raiz)))

# math.ceil(x): arredonda o número para cima. Ex: de 2.2360... ele passa para 3.
# math.floor(x): arredonda para baixo.
# Se eu uso 'from x import a1, a2, ...', eu não preciso usar 'x.a1()' no comando, pois
# ele vem direto na pasta para ser usado, o caso não acontece se importar a biblioteca
# toda. Ex:

# IMPORT PREFERENCES:
# from math import sqrt
# raiz = sqrt(num)

# IMPORT ALL:
# import math
# raiz = math.sqrt(num)