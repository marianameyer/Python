# Escreva um programa que leia um número inteiro qualquer e peça para o usuário para escolher qual será a base de
# conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

# Coleta de dados do usuário:
num = int(input('Digite o número inteiro a ser convertido: '))
conv = str(input('Bases disponíveis para a conversão: \n\033[33m1\033[m => Binário'
                 '\n\033[32m2\033[m => Octal \n\033[35m3\033[m => Hexadecimal \nQual sua opção? '))

# Conversões
if conv == '1':
    print(f'O número \033[33m{num}\033[m convertido para binário é igual a \033[33m{num:b}\033[m.')
elif conv == '2':
    print(f'O número \033[32m{num}\033[m convertido para octal é igual a \033[32m{num:o}\033[m.')
elif conv == '3':
    print(f'O número \033[35m{num}\033[m convertido para hexadecimal é igual a \033[35m{num:x}\033[m.')
else:
    print(f'A opção \033[31m{conv}\033[m é \033[4;31minválida\033[m! Escolha outra conversão...')
