# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo,
# cadastrando tudo em uma lista composta

import random

jogos = list()
for ele in range(0, int(input('Digite: '))):
    jogos.append([random.randint(0, 60) for _ in range(6)])
print(jogos)
