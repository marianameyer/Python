# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.

# Se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo

# Coleta de dados do usuário
l1 = int(input('Digite o primeiro comprimento: '))
l2 = int(input('Digite o segundo comprimento: '))
l3 = int(input('Digite o terceiro comprimento: '))

# Condicionais
if (l1 + l2 > l3) and (l2 + l3 > l1) and (l1 + l3 > l2):
    print('Com as três medidas informadas, \033[1:32mpode-se formar\033[m um triângulo.')  # Add colors
else:
    print('Com as três medidas informadas, \033[1;31mnão é possível formar\033[m um triângulo.')  # Add colors
