# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Importando a biblioteca
import random

# Coleta de dados do usuário
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
a4 = input('Quarto nome: ')

# Criação da lista com o nome dos alunos
alunos = [a1, a2, a3, a4]

# Lista gerada aleatoriamente pelo programa - k=tamanho da lista
al = random.sample(alunos, k=4)

# Print
print(f'A ordem de apresentação dos trabalhos será: \n{al[0]}; \n{al[1]}; \n{al[2]}; \n{al[3]}.')
