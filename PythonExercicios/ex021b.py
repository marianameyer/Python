# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
# Usando o PyGame - Funcionou lindinho!

# Importando a biblioteca
import pygame

# Tocando o áudio sample.mp3
pygame.mixer.init()
pygame.init()  # Não é necessário para funcionar!
pygame.mixer.music.load('sample.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)  # Não é necessário para funcionar!

# Para o som ser tocado, temos duas opções: esperar a música terminar, ou dar um comando:
# pygame.event.wait()  # Sem esse comando, o som não é tocado! O programa pára quando o música termina
x = input('Digite algo para encerrar: ')  # Sem esse input, o som não é tocado!
