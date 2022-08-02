# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar no serviço militar;
# se é a hora de se alistar;
# se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Importando biblioteca
import datetime

# Coletando dados do usuário - Ano e sexo do usuário
ano_nascimento = int(input('Digite o ano de nascimento: '))
sexo = str(input('Qual seu sexo? (M/F) ')).strip()
sex = sexo.lower()

# Supondo alistamento obrigatório no ano em que completa-se 18 anos
ano_atual = datetime.datetime.today().year
idade = ano_atual - ano_nascimento
ano_alistamento = ano_nascimento + 18
print(f'Quem nasceu em {ano_nascimento} possui {idade} no ano de {ano_atual}.')

# Condicionais
if sex == 'm':
    if idade < 18:
        print(f'Ainda faltam {18 - idade} anos para o alistamento. \nSeu alistamento será em {ano_alistamento}.')
    elif idade == 18:
        print('Já está na hora de se alistar!')
    else:
        print(f'Já se passaram {idade - 18} anos que você deveria ter se alistado. \nSeu alistamento foi em '
            f'{ano_alistamento}.')
elif sex == 'f':
    print('No Brasil, o alistamento militar não é obrigatório para mulheres.')
