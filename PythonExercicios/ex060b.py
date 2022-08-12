# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Fiz de outra forma
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# Coleta de dado do usuário
num = int(input('Digite um número: '))

# Contador do while e variável fatorial
j = num - 1

# Verificação do fatorial de 0
if num != 0:
    fatorial = num
else:
    fatorial = 1

# Saída como no exemplo
print(f'{num}! = {num} ', end='')

while j >= 1:
    if j != 1:
        print(f'x {j} ', end='')
        fatorial = fatorial * j
        j -= 1
    else:
        print(f'x {j} = {fatorial}')
        break
