# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# abaixo de 18.5: ABAIXO DO PESO
# entre 18.5 e 25: PESO IDEAL
# entre 25 e 30: SOBREPESO
# 30 até 40: OBESIDADE
# acima de 40: OBESIDADE MÓRBIDA

# Coleta de dados do usuário
peso = float(input('Qual o seu peso (em kg)? '))
alt = float(input('Qual a sua altura (em m)? '))

# Operações
imc = peso / (alt ** 2)

# Condicionais
if imc < 18.5:
    print('\033[1;33mABAIXO DO PESO\033[m')
elif imc < 25:
    print('\033[1;32mPESO IDEAL\033[m')
elif imc < 30:
    print('\033[1;33mSOBREPESO\033[m')
elif imc < 40:
    print('\033[1;31mOBESIDADE\033[m')
else:
    print('\033[7;31mOBESIDADE MÓRBIDA\033[m')
