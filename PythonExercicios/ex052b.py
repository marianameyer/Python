# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Resolução do Curso em Vídeo - FOR

# Coleta de dado do usuário
num = int(input('Digite um número inteiro: '))

# Contadores
count_div = 0

# Loop for
for c in range(1, num+1):
    if num % c == 0:
        count_div += 1
    else:
        pass

# Verificação de número primo (é divisível apenas por 1 e por ele mesmo)
if count_div == 2:
    print(f'O núemro {num} É PRIMO!')
else:
    print(f'O número {num} NÃO É PRIMO...')
