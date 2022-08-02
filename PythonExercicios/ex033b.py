# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Solução do Curso em Vídeo:

# Coleta de dados do usuário
n1 = int(input('\033[1;35mDigite o primeiro número:\033[m '))
n2 = int(input('\033[1;36mDigite o segundo número:\033[m '))
n3 = int(input('\033[1;33mDigite o terceiro número:\033[m '))

# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O \033[4;30;42mmenor\033[m número é o \033[1;32m{menor}\033[m.')
print(f'O \033[4;30;41mmaior\033[m número é o \033[1;31m{maior}\033[m.')
