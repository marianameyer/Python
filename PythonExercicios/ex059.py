# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

# Coleta de dados do usuário
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

# Início da calculadora
option = 1

# Loop While
while option != 5:
    print('=-' * 20)
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
    option = int(input('Qual a sua opção? '))
    if option == 1:
        print(f'{num1} + {num2} = {num1+num2}')
    elif option == 2:
        print(f'{num1} x {num2} = {num1*num2}')
    elif option == 3:
        print(f'O maior número informado é {max(num1, num2)}')
    elif option == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    else:
        print('Essa opção não existe...Digite uma opção válida:')
print('=-' * 20)
print('TCHAU!!!')
