# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles. (tentar colocar emoji)

# Importando bibliotecas
from time import sleep
import emoji

# Saída do usuário
print('Contagem Regressiva!')
for i in range(10, 0, -1):
    print(f'{i}!')
    sleep(1)
print(emoji.emojize(':fireworks: :fireworks: :fireworks:'))
