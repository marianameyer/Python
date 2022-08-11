# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Importando a biblioteca
from random import randint

# Início
print('*.*'*12)
print('\t\t\033[1;32mJOGO DA ADIVINHAÇÃO\033[m')
print('*.*'*12)
print('\nO computador pensou em um número entre 0 e 10.')

# Jogada do computador
num_pc = randint(0, 10)

# Jogada do usuário
num_jog = int(input('Qual número o computador pensou? '))

# Contador de jogadas
count_jogadas = 1

# Jogo
while num_jog != num_pc:
    num_jog = int(input('Hum, não foi esse o número escolhido. Tente outra vez: '))
    count_jogadas += 1

print(f'\nApós \033[1;33m{count_jogadas}\033[m jogadas você adivinhou o número escolhido pelo '
      f'computador: \033[1;34m{num_pc}\033[m!')
