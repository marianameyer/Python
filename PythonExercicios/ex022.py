# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiúsculas
# 2) O nome com todas as letras minúsculas
# 3) Quantas letras ao todo (sem contar espaços)
# 4) Quantas letras tem o primeiro nome

# Coleta de dados do usuário
nome_comp = str(input('Digite seu nome completo: ')).strip()  # Retira espaços indesejados
nome_listado = nome_comp.split()
nome_junto = ''.join(nome_listado)

# Prints
print(f'Em maiúsculas: {nome_comp.upper()}.')
print(f'Em minúsculas: {nome_comp.lower()}.')
print(f'Seu nome completo possui {len(nome_junto)} letras.')
print(f'O primeiro nome ({nome_listado[0]}) possui {len(nome_listado[0])} letras.')
