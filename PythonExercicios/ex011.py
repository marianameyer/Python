# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

# Coleta de dados do usuário
alt = float(input('Qual a altura da parede, em metros? '))
larg = float(input('Qual a largura da parede, em metros? '))

# Cálculo da área a ser pintada e da quantidade de litros necessários
area = alt * larg
lit = area / 2

# Print
print(f'\nUma parede com {alt} m de altura e {larg} m de largura possui área igual a {area} m².')
print(f'Portanto, você precisará de {lit:.2f} litros de tinta.')
