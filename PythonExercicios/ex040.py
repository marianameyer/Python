# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# média abaixo de 5.0: REPROVADO
# média entre 5.0 e 6.9: RECUPERAçÃO
# média 7.0 ou superior: APROVADO

# Coleta de dados do usuário
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Operação
media = (n1 + n2) / 2

# Condicionais
if media < 5.0:
    print('\033[1;31mREPROVADO\033[m.')
elif (media >= 5.0) and (media < 6.9):
    print('\033[1;33mRECUPERAÇÃO\033[m.')
elif media >= 7.0:
    print('\033[1;32mAPROVADO\033[m.')
