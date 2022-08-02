# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

# Contador
soma = 0

# Coleta de dados do usuário
for c in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
    else:
        pass
print(f'A soma dos números pares informados é igual a {soma}.')
