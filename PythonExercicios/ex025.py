# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

# Coleta e manipulação de dados do usuário
nome = str(input('Digite seu nome: ')).strip()

# Print
print(f'É verdade que o nome {nome} possui o nome Silva? {"silva" in nome.lower()}')
