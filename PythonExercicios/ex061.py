# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
#
# DESAFIO 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.
# an = a1 + (n - 1) * r

# Coleta de dados do usuário
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
tam = int(input('Quantos elementos da PA você quer que sejam mostrados? '))

# Contador e saída
n = 1
print(f'\nOs {tam} primeiros elementos da PA dada são:')

# Loop while
while n <= tam:
    an = a1 + (n - 1) * r
    if n < tam:
        print(f'{an}, ', end='')
        n += 1
    else:
        print(f'{an}.')
        break
