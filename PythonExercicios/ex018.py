# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

# Importando a biblioteca math (para variar um pouco)
import math

# Coletando dado do usuário
ang = float(input('Digite o ângulo (em graus): '))

# Vamos converter o ângulo de graus para radianos (As funções do math são calculadas em radianos).
tetha = math.radians(ang)

# Print - Precisão de 2 casas decimais
print(f'Para o ângulo de {ang}º, temos: \nSeno: {math.sin(tetha):.2f}. \nCosseno: {math.cos(tetha):.2f}.'
      f'\nTangente: {math.tan(tetha):.2f}.')
