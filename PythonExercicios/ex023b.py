# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex.: Digite um número 1834
# Unidade: 4 / Dezena: 3 / Centena: 8/ Milhar: 1

# Teste - Usando funções matemáticas - Gambiarra tbm

# Coleta e manipulação dos dados
num = int(input('Digite um número de 0 a 9999: '))
mil = int(num/1000)
cent = int(num/100) - 10*mil
dez = int(num/10) - 100*mil - 10*cent
un = num - 1000*mil - 100*cent - 10*dez

print(f'Unidade: {un}. \nDezena: {dez}. \nCentena: {cent}. \nMilhar: {mil}.')
