# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo pc. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Importando a biblioteca
import random

# Geração do número pelo computador
num_pc = random.randint(0, 5)

# Input usuário
num_u = int(input('Qual número o computador escolheu? Dica: foi um número entre 0 e 5: '))

# Condicionais
if num_u == num_pc:
    print('Parabéns! Você acertou o número escolhido pelo computador!')
else:
    print(f'Que pena! Você perdeu! \nVocê escolheu {num_u}, enquanto o computador escolheu {num_pc}.')
