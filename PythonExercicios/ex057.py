# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

# Coleta de dado do usuário
sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Esta opção não existe. Qual seu sexo? [M/F] ')).upper().strip()

print(f'Sexo informado: {sexo}. Obrigada!')
