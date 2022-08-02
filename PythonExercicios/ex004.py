# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
# as informações possíveis sobre ela.
algo = input('Digite algo: ')
print(f'O tipo primitivo é: {type(algo)}')
print(f'É composta apenas por espaços? {algo.isspace()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'É numérico? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'Está em minúsculo? {algo.islower()}')
print(f'Está em maiúsculo? {algo.isupper()}')
print(f'Está capitalizada? {algo.istitle()}')
