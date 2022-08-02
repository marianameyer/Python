# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 25 anos: SÊNIOR
# acima: MASTER

# Carregando biblioteca
from datetime import date

# Coleta de dado do usuário
ano_nascimento = int(input('Qual o ano de nascimento do atleta? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f'O atleta possui {idade} anos. \nEle competirá na categoria: ', end='')

# Condicionais
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')
