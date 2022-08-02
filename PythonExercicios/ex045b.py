# Crie um programa que faça o computador jogar Jokenpô com você.
# Versão feita usando lista.

# Importando bibliotecas
from random import randint
from time import sleep

# Firula
print('='*40)
print(f'\033[1;33m{"JO KEN PÔ":^40}\033[m')
print('='*40)

# Lista com opções das jogadas
op = ['PEDRA', 'PAPEL', 'TESOURA']

# Jogada do computador
j_pc = randint(0, 2)
pc = op[j_pc]

# Coleta de dados do usuário
print('\nVamos jogar Jokenpô? Temos as três opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')
j_u = int(input('Qual sua jogada? '))

# Verificação de opção válida e início do jogo
if j_u != 0 and j_u != 1 and j_u != 2:
    print(f'A opção \033[1;31m{j_u}\033[m não é uma opção válida! \nEscolha outro número!')
else:
    jog = op[j_u]
    sleep(0.5)
    print('\n\033[1;33mJO\033[m')
    sleep(0.2)
    print('\t\033[1;32mKEN\033[m')
    sleep(0.2)
    print('\t\t\033[1;31mPÔ\033[m\n')
    sleep(0.5)
# Condicionais do jogo
    if pc == jog:  # Verificação de empate
        print(f'\033[1;33mEMPATE!\033[m Ambos jogaram \033[35m{jog}\033[m!')
    elif (j_u == 0 and j_pc == 2) or (j_u == 1 and j_pc == 0) or (j_u == 2 and j_pc == 1):  # Verificação de ganho
        print(f'\033[1;32mVOCÊ VENCEU!\033[m Você jogou \033[35m{jog}\033[m e o computador jogou \033[35m{pc}\033[m.')
    else:  # Verificação de perda
        print(f'\033[1;31mVOCÊ PERDEU!\033[m Você jogou \033[35m{jog}\033[m e o computador jogou \033[35m{pc}\033[m.')
print('Obrigado por jogar!')
