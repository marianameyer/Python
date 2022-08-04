# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
# FOR - Resolução Curso em Vídeo

# Contadores
maior = 0
menor = 0

# Coleta de dado dos usuários
for c in range(1, 6):
    peso = float(input(f'Qual o peso da {c}ª pessoa? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior} kg e o menor peso foi de {menor} kg.')
