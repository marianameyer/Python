# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos.

# Contadores e somadores
cont_idade = 0
homem_velho = 0
idade_homem_velho = 0
cont_m = 0

# Coleta de dados dos usuários
for c in range(1, 5):
    nome = str(input(f'Qual o nome da {c}ª pessoa? ')).strip()
    idade = int(input(f'Qual a idade da {c}ª pessoa? '))
    sexo = str(input(f'Qual o sexo da {c}ª pessoa? [m/f] ')).lower()

    # Contador para a média das idades
    cont_idade += idade

    # Verificação do homem mais velho
    if sexo == 'm':
        if c == 1:
            homem_velho = nome
            idade_homem_velho = idade
        else:
            if idade > idade_homem_velho:
                idade_homem_velho = idade
                homem_velho = nome

    # Verificação de quantas mulheres têm menos de 20 anos
    if sexo == 'f':
        if idade < 20:
            cont_m += 1

# Média da idade do grupo
media_idade = cont_idade / 4

# Saída
print(f'A média de idade do grupo informado é igual a {media_idade:.1f} anos.')
print(f'O homem mais velho do grupo é o {homem_velho} com {idade_homem_velho} anos.')
print(f'No grupo informado há {cont_m} mulheres com menos de 20 anos.')
