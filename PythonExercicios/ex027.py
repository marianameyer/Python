# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente. Ex.: Ana Maria de Souza
# primeiro: Ana / último: Souza

# Coleta e manipulação de dados do usuário
nome = str(input('Digite o nome completo: ')).strip()
nome_div = nome.split()

# Print
print(f'Primeiro: {nome_div[0]}. \nÚltimo: {nome_div[len(nome_div)-1]}.')
