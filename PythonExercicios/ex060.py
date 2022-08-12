# Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# Coleta de dado do usuário
num = int(input('Digite um número: '))

# Contador do while
j = 1

# Verificação do fatorial de 0
if num == 0:
    fatorial = 1
else:
    fatorial = num

# Loop while
while j < num:
    fatorial = fatorial * j
    j += 1

# Saída do usuário
print(f'O fatorial de {num} é igual a {fatorial}.')
