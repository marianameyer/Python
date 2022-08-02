# Crie um programa que faça o computador jogar Jokenpô com você.

# Importando biblioteca
from random import randint

# Firula
print('='*20)
print('\t\033[1;31mJO\033[m \033[1;33mKEN\033[m \033[1;32mPÔ\033[m')
print('='*20)

# Geração aleatória do pc
pc = randint(1, 3)

# Coleta de dado do usuário
print('\nEscolha uma das opções para jogar: \n[ 1 ] \033[34mPedra\033[m \n[ 2 ] \033[35mPapel\033[m '
      '\n[ 3 ] \033[36mTesoura\033[m')
jogador = int(input('Qual sua opção? '))

# Condicionais
if (pc == 1) and (jogador == 3):
    print('Você escolheu \033[1;33mtesoura\033[m e o computador escolheu \033[1;33mpedra\033[m. '
          '\nVocê \033[1;31mPERDEU\033[m!')
elif (pc == 2) and (jogador == 1):
    print('Você escolheu \033[1;33mpedra\033[m e o computador escolheu \033[1;33mpapel\033[m. '
          '\nVocê \033[1;31mPERDEU\033[m!')
elif (pc == 3) and (jogador == 2):
    print('Você escolheu \033[1;33mpapel\033[m e o computador escolheu \033[1;33mtesoura\033[m. '
          '\nVocê \033[1;31mPERDEU\033[m!')
elif pc == jogador:
    print('Ambos fizeram a mesma escolha! \nJogo \033[1;33mEMPATADO\033[m!')
else:
    print('Parabéns! Você \033[1;32mGANHOU\033[m!')
