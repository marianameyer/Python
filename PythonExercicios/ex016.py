# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
# Ex.: Digite um número: 6.127
#      O número 6.127 tem a parte inteira 6.

# Importando pacote floor do math
from math import floor

# Coleta do dado
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {floor(num)}')

'''print(f'O número {num} tem a parte inteira {int(num)}.')  # Outra opção
   print(f'O número {num} tem a parte inteira {math.trunc(num)}.')  # Outra opção'''
