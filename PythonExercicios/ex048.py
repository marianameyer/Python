# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no
# intervalo de 1 até 500.

# Saída do usuário
print('Números ímpares múltiplos de 3:')
soma = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            print(c)
            soma += c
        else:
            pass
    else:
        pass
print(f'A soma de todos os números ímpares múltiplos de 3 é igual a {soma}.')
print('FIM!')
