# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela
# pode comprar.
# Considere: US$ 1,00 = R$ 3,27

# Coleta de dados do usuário
din = float(input('Quanto dinheiro você possui na carteira? R$'))

# Print
print(f'Com R${din} você pode comprar US${din/3.27:.2f}.')
