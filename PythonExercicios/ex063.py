# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci.
#
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

# Início
print('=-='*14)
print('\t\tSEQUÊNCIA DE FIBONACCI')
print('=-='*14)

# Coleta de dado do usuário
n = int(input('Quantos termos da sequência você quer ver? '))

# Contadores
count = 3  # Primeiro e segundo termos serão mostrados a seguir
seq = 0  # Termo atual
seq_1 = 1  # Termo -1
seq_2 = 0  # Termo -2

# Saída do usuário
print(f'{seq_2} -> {seq_1} -> ', end='')

# Loop
while count <= n:
    seq = seq_1 + seq_2
    print(f'{seq} -> ', end='')
    seq_2 = seq_1
    seq_1 = seq
    count += 1
print('FIM!')
