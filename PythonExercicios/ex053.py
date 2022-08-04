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

# Lista e Contador
lista = []
count = 0

# Laço for
for letra in frase:
    lista.append(letra)

# Definindo tamanho da lista e criando uma lista inversa
fim = len(lista)
lista_reversa = lista[::-1]

# Analisando se os itens da lista e da lista inversa são iguais
for i in range(0, fim):
    if lista[i] == lista_reversa[i]:
        count += 1
    else:
        pass

# Verificação se a frase digitada é ou não um palíndromo
if count == fim:
    print('A frase digitada É um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo...')
