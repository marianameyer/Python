# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
# an = a1 + (n - 1) * r

# Coleta de dado do usuário
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

# Lista com os 10 primeiros elementos da PA
pa = [a1]

# Laço for
for c in range(2, 11):
    an = a1 + (c - 1) * r
    pa.append(an)
print(f'Uma PA com primeiro elemento igual a {a1} e razão igual a {r} possui os 10 primeiros elementos: {pa}.')
