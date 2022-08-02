# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Palíndromo: lido normal == lido de trás para frente
# Ex.: Apos a sopa ; a sacada da casa ; a torre da derrota ; o lobo ama o bolo ; anotaram a data da maratona

# Coleta de dados do usuário
frase = str(input('Digite uma frase para saber se ela é ou não um palíndromo: ')).strip()

# Tratamento da entrada
frase = frase.lower()
frase = frase.replace(' ', '')
frase = frase.replace('á', 'a')
frase = frase.replace('ã', 'a')
frase = frase.replace('é', 'e')
frase = frase.replace('ó', 'o')
print(frase)

# Laço
for c in range(len(frase)+1, 0, -1):
    print(c)
