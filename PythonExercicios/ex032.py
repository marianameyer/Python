# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Coleta de dados do usuário
ano = int(input('Digite um ano: '))

# Condicionais para verificar se o ano é bissexto
if (ano % 4 == 0):
    if (ano % 100 != 0):
        print(f'O ano de {ano} é bissexto!')
    else:
        if (ano % 400 == 0):
            print(f'O ano de {ano} é bissexto!')
        else:
            print(f'O ano de {ano} não é bissexto...')
else:
    print(f'O ano de {ano} não é bissexto...')
