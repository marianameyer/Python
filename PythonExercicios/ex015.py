# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Coleta de dados do usuário
diaria = int(input('Por quantos dias o carro ficou alugado? '))
km_percorrido = float(input('Qual a distância [km] percorrida neste tempo? '))

# Cálculo
total_diaria = diaria * 60
total_km_percorrido = km_percorrido * 0.15
valor_total = total_diaria + total_km_percorrido

# Print
print(f'Olá! O carro percorreu {km_percorrido}km em {diaria} dias.')
print(f'O valor total do aluguel ficou em R${valor_total:.2f}.')
