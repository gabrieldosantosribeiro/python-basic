#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10
# e continue pedindo até que o usuário acerte o número.
# E no final, retorne também a quantidade de tentativas necessárias.
'''
import random

numero = random.randint(1, 10)
tentativa = None
contagem = 0
print(numero)
while tentativa != numero:
    tentativa = int(input('digite um numero: '))
    contagem += 1
print(f'você tentou {contagem} vezes até acertar.')

'''

import random
try:
    aleatorio = random.randint(1, 10)
    jogador = ''
    contagem = 1
    while aleatorio != jogador:
        jogador = int(input('Digite seu palpite: '))

        if aleatorio == jogador:
            print(f'Você Acertou!! Precisou de {contagem} vezes')
        else:
            print('Você Errou')
            contagem += 1
except ValueError:
    print('Apenas números inteiros.')



