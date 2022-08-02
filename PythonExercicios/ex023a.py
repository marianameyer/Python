# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex.: Digite um número 1834
# Unidade: 4 / Dezena: 3 / Centena: 8/ Milhar: 1

# Versão Gambiarra

# Coleta de dados do usuário
num = str(input('Digite um número de 0 a 9999: '))  # Usei str() para poder dividir por index
num2 = 10000
n = str(num2)+num

# Print
print(f'Unidade: {n[-1]}. \nDezena: {n[-2]}. \nCentena: {n[-3]}. \nMilhar: {n[-4]}.')
