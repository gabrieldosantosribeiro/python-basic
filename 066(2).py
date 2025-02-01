# Crie um programa que crie uma matriz de dimensão 3x3 e
# preencha com valores lidos pelo teclado.
# No final mostre a matriz na tela, com a formatação correta
try:
    matriz = list()
    matriz.append([int(input('digite:')) for ele in range(9)])
    matriz = sorted(matriz[0])
    for ele in range(3):

        print(matriz)
except ValueError:
    print('Apenas números')
