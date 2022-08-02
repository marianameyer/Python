# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

# Coleta e manipulação de dados do usuário
cidade = str(input('Qual o nome da cidade? ')).strip()
div = cidade.lower().split()

# Print
print(f'A cidade {cidade} possui Santo no primeiro nome? {"santo" in div[0]}')
