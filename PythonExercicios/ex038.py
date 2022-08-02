# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.

# Coleta de dados do usuário
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

# Condicionais
if num1 > num2:
    print('O \033[1;33mprimeiro\033[m valor é \033[1;33mmaior\033[m.')
elif num2 > num1:
    print('O \033[1:33msegundo\033[m valor é \033[1;33mmaior\033[m.')
else:
    print('Não existe valor maior, os são \033[1;33miguais\033[m!')
