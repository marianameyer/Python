# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# Resolução com saída igual ao do Curso em Vídeo

# Importando a biblioteca
from random import randint

# Início
print('Sou seu computador... \nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

# Jogada do computador
num_pc = randint(0, 10)
print(num_pc)

# Jogada do usuário
num_jog = int(input('Qual é seu palpite? '))

# Contador de jogadas
count_jog = 1

# Jogo
while num_jog != num_pc:
    if num_jog > num_pc:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
    num_jog = int(input('Qual é seu palpite? '))
    count_jog += 1

print(f'Acertou com {count_jog} tentativas. Parabéns!')
