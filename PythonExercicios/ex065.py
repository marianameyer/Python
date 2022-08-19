# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores. -> Não usar lista!

# Início
print('~'*42)
print('\t\tMÉDIA - MÁXIMO - MÍNIMO')
print('~'*42)

# Contadores
count = 0  # Contador de números inseridos
soma = 0  # Soma os números inseridos
num = 0  # Variável de entrada
continua = 's'  # Variável de loop
maior = menor = 0  # Variáveis para maior e menor números informados

# Loop
while continua[0] == 's':
    num = int(input('Digite um número inteiro: '))
    soma += num
    if count == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    count += 1
    continua = str(input('Gostaria de digitar mais valores? [S/N] ')).strip().lower()
    if continua[0] == 'n':
        break

# Cálculos
media = soma / count

# Saída
print('~'*42)
print(f'\t\tDADOS OBTIDOS: \nNúmeros Informados: {count}. \nMédia: {media:.2f}.')
print(f'Maior número informado: {maior}. \nMenor número informado: {menor}.')
