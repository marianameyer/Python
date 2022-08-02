# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# Equação: C = 5 * ( F - 32) / 9   \\\  F = C * (9/5) + 32

# Coleta de dado do usuário
c = float(input('Qual a temperatura em Celsius? '))

# Cálculo
f = c * (9/5) + 32

# Print
print(f'A temperatura de {c}ºC equivale a {f:.1f}ºF.')
