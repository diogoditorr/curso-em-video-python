# Lê o nome de 4 alunos e mostra a ordem de sorteio
import random

n1 = str(input('Primeiro: '))
n2 = str(input('Segundo: '))
n3 = str(input('Terceiro: '))
n4 = str(input('Quarto: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'Primeiro a apresentar: {lista[0]}'
      f'\nSegundo a apresentar:{lista[1]}'
      f'\nTerceiro a apresentar: {lista[2]}'
      f'\nQuarto a apresentar: {lista[3]}')
