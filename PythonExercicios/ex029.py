# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

# Coleta dos dados
velocidade = float(input('Qual a velocidade do carro, em km/h? '))

# Condicionais
if velocidade > 80:
    valor = (velocidade - 80)* 7
    print(f'Você está acima da velocidade! Sua velocidade atual é igual a {velocidade} km/h!'
          f'\nVocê será multado em R${valor:.2f}.')
else:
    print(f'Que orgulho! Você está dentro do limite permitido de velocidade!')
