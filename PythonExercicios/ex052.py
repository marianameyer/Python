# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Usarei o Crivo de Erastótenes - IF

# Coleta de dado do usuário
num = int(input('Digite um número inteiro: '))

# Condicionais
if num == 1:
    print(f'{num} NÃO é primo!')
elif (num != 2) and (num % 2 == 0):
    print(f'{num} NÃO é primo!')
elif (num != 3) and (num % 3 == 0):
    print(f'{num} NÃO é primo!')
elif (num != 5) and (num % 5 == 0 or num % 10 == 0):
    print(f'{num} NÃO é primo!')
elif (num != 7) and (num % 7 == 0):
    print(f'{num} NÃO é primo!')
else:
    print(f'{num} É primo!')
