# Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que o ajude, lendo o
# nome dos alunos e escrevendo o escolhido.

# Importando a biblioteca
import random

# Coletando os dados do usuário
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
a4 = input('Quarto e último nome: ')

# Print - Usei o random.choice e criei uma lista dentro dele...
print(f'O nome escolhido foi {random.choice([a1, a2, a3, a4])}.')
