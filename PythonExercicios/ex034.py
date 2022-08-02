# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# Coleta de dados do usuário
salario = float(input('\033[1;33mQual o salário do funcionário?\033[m R$'))

# Condicionais
if salario > 1250:
    valor = salario * 1.1
    print(f'O salário de R${salario} terá um reajuste de 10%. '
          f'\nLogo, o novo salário será igual a \033[1;34mR${valor:.2f}\033[m.')
else:
    valor = salario * 1.15
    print(f'O salário de R${salario} terá um reajuste de 15%. '
          f'\nLogo, o novo salário será igual a \033[1;34mR${valor:.2f}\033[m.')
