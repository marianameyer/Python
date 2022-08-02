# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex.: Digite um número 1834
# Unidade: 4 / Dezena: 3 / Centena: 8/ Milhar: 1

# Teste - Usando funções matemáticas - Modelo matematicamente mais elegante!

num = int(input('Digite um número de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}. \nDezena: {d}. \nCentena: {c}. \nMilhar: {m}.')
