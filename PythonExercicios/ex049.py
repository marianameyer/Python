# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora usando um laço for.
# Desafio 009: Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

# Coleta de dado do usuário
num = int(input('Digite um número para saber sua tabuada: '))

print('-'*14)

# Laço
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c:3}.')
print('-'*14)
