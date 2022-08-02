# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
# negado.

# Coleta de dados do uusário
valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = float(input('Em quantos anos pretende quitar a casa? '))

# Análise dos dados
valor_prestacao = valor / (anos * 12)  # Valor da prestação mensal
sal_30 = sal * 0.7  # 30% do salário do comprador

print(f'Para pagar uma casa de \033[33mR${valor:.2f}\033[m em \033[33m{anos:.1f} anos\033[m'
      f' a prestação será de \033[33mR${valor_prestacao:.2f}\033[m.')
# Condicionais
if valor_prestacao <= sal_30:
    print('\033[1;32mEMPRÉSTIMO APROVADO!\033[m')
else:
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m')
