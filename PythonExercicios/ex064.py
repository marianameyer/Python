# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag).

# Contador
count = 0  # Contador de números digitados
num = 0  # Números coletados pelo usuário
soma = 0  # Soma dos números coletados

# Coleta de dados do usuário
while num != 999:
    num = int(input('Digite um número inteiro: [999 para parar] '))
    if num != 999:
        soma += num
        count += 1
    elif num == 999:
        break
print(f'Foram digitados {count} números, que somados totalizaram {soma}.')
