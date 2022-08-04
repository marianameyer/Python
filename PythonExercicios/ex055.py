# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
# FOR e Lista

# Lista com os pesos
lista_pesos = []

# Coleta de dado dos usuários
for c in range(1, 6):
    peso = float(input(f'Qual o peso da {c}ª pessoa? '))
    lista_pesos.append(peso)

# Ordenando os valores na lista
lista_pesos.sort()

print(f'O maior peso lido foi de {lista_pesos[4]}kg e o menor peso foi de {lista_pesos[0]}kg.')
