# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'a';
# Em que posição ela aparece a primeira vez;
# Em qual posição ela aparece a última vez.

# Coleta de dados do usuário
frase = str(input('Digite uma frase: ')).strip()
frase_nova = frase.lower().replace('á', 'a').replace('ã', 'a').replace('à', 'a')
first = frase_nova.find("a")
last = frase_nova.find("a", -1, 0)

# Print
print(f'A frase digitada possui {frase_nova.count("a")} letras a.')
print(f'A letra a aparece a primeira vez na posição {first+1} e na última vez na posição {len(frase_nova)+last+1}.')
