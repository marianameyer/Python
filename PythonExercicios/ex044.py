# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

# Firula
print(f'{"LOJAS GUANABARA":=^40}')  # Escrita centralizada

# Coleta de dados
valor = float(input('Qual o valor do produto? R$'))
print('Temos 4 formas de pagamento: \n[ 1 ] À vista dinheiro/cheque \n[ 2 ] À vista cartão \n[ 3 ] 2x no cartão '
      '\n[ 4 ] 3x ou mais no cartão')
pag = int(input('Qual será a forma de pagamento? '))

# Condicionais
if pag == 1:
    valor_final = valor * 0.9
    print(f'A opção de pagamento à vista no cheque ou em dinheiro dá 10% de desconto! '
          f'\nSua compra no valor de R${valor:.2f} sairá por R${valor_final:.2f}.')
elif pag == 2:
    valor_final = valor * 0.95
    print(f'A opção de pagamento à vista no cartão dá 5% de desconto! '
          f'\nSua compra no valor de R${valor:.2f} sairá por R${valor_final:.2f}.')
elif pag == 3:
    valor_final = valor
    valor_parc = valor_final / 2
    print(f'Sua compra será parcelada em 2 vezes, sem acréscimo de juros. '
          f'\nO valor da parcela será igual a R${valor_parc:.2f}. e o total será de R${valor_final:.2f}.')
elif pag == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor_final = valor * 1.2
    valor_parc = valor_final / parcelas
    print(f'Sua compra será parcelada em {parcelas} vezes de R${valor_parc:.2f}. '
          f'\nSua compra no valor de R${valor:.2f} custará R${valor_final:.2f}.')
else:
    print(f'Não existe a opção {pag}. Por favor, insira uma opção válida.')
