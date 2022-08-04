# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
# Considerar maioridade == 21 anos

# Importando biblioteca
from datetime import date

# Ano atual
ano_atual = date.today().year

# Contadores
count_maior = 0
count_menor = 0

# Coleta de dado dos usuários
for c in range(1, 8):
    ano = int(input(f'Em qual ano nasceu a {c}ª pessoa? '))
    idade = ano_atual - ano
    if idade >= 21:
        print(f'A {c}ª pessoa é maior de idade, uma vez que ela possui {idade} anos.')
        count_maior += 1
    else:
        count_menor += 1
print(f'Das sete pessoas entrevistadas, {count_menor} não atingiram a maioridade e {count_maior} são maiores de idade.')
