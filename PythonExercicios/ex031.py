# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50
# por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

# Coleta de dados do usuário
dist = float(input('Qual a distância (em km) será percorrida na sua viagem? '))

# Condicionais
if dist <= 200:
    valor_menor = dist * 0.5
    print(f'Para uma distância de {dist:.2f} km, você pagará R$ {valor_menor:.2f}.')
else:
    valor_maior = dist * 0.45
    print(f'Para uma distância de {dist:.2f} km, você pagará R$ {valor_maior:.2f}.')
