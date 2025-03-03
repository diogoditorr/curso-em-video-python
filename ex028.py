# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tecla se o usuário venceu ou perdeu

import random

print('Vamos jogar um jogo?'
      '\n'
      '\nPensei em um número entre 0 e 5'
      '\nQue número eu pensei?')
choice_computer = int(random.randint(0, 5))
choice_player = int(input(''))

if choice_computer == choice_player:
    print('Parabéns! Você venceu!')
else:
    print(f'Sinto muito, você perdeu. O número que pensei foi {choice_computer} ;(')
