# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Coleta de dados do usuário
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Condicionais
if (n1 > n2) and (n1 > n3):
    if (n2 > n3):
        print(f'O maior número é o {n1} e o menor é o {n3}.')
    else:
        print(f'O maior número é o {n1} e o menor é o {n2}.')
if (n2 > n1) and (n2 > n3):
    if (n1 > n3):
        print(f'O maior número é o {n2} e o menor é o {n3}.')
    else:
        print(f'O maior número é o {n2} e o menor é o {n1}.')
if (n3 > n1) and (n3 > n2):
    if (n1 > n2):
        print(f'O maior número é o {n3} e o menor é o {n2}.')
    else:
        print(f'O maior número é o {n3} e o menor é o {n1}.')
else:
    print('Os três números devem ser diferentes!')
