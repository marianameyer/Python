# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.

# Importação do pacote sqrt e pow do math
from math import sqrt, pow

# Coletando os dados do usuário
cat_o = float(input('Qual o comprimento do cateto oposto? '))
cat_a = float(input('Qual o comprimento do cateto adjacente? '))

# Cálculo da hipotenusa
hip = sqrt(pow(cat_o, 2) + pow(cat_a, 2))

# Print
print(f'Com cateto oposto igual a {cat_o} e cateto adjacente igual a {cat_a}, a hipotenusa possui comprimento '
      f'igual a {hip}.')
# Outra maneira com a biblioteca math
# print(f'Com cateto oposto igual a {cat_o} e cateto adjacente igual a {cat_a}, a hipotenusa possui comprimento '
#       f'igual a {math.hypot(cat_a, cat_o)}.')
