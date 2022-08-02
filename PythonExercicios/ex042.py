# Refaça o desafio 35, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# equilátero: todos os lados iguais
# isósceles: dois lados iguais
# escaleno: todos os lados diferentes

# Coleta dos dados
l1 = int(input('Digite o primeiro tamanho: '))
l2 = int(input('Digite o segundo tamanho: '))
l3 = int(input('Digite o terceiro tamanho: '))

# Condicionais para verificar se as retas podem formar um triângulo
if (l1 + l2 > l3) and (l2 + l3 > l1) and (l1 + l3 > l2):
    print('Com as três medidas, temos um triângulo! \nMas qual tipo de triângulo?? ')
    # Condicionais para verificação do tipo de triângulo
    if l1 == l2 == l3:
        print('Um triângulo \033[1;33mEQUILÁTERO\033[m!')
    elif (l1 == l2) or (l2 == l3) or (l1 == l3):
        print('Um triângulo \033[1;33mISÓSCELES\033[m!')
    elif l1 != l2 != l3:
        print('Um triângulo \033[1:33mESCALENO\033[m!')
else:
    print('Com as três medidas, \033[1;31mNÃO É POSSÍVEL\033[m formar um triângulo!')
