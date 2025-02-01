# Escreva um programa que verifique se uma palavra é um palíndromo.

palavra = input('digite uma palavra: ').strip().lower()
quantidade = len(palavra)
contador = 0

if palavra[contador] == palavra[quantidade-1]:
    for ele in range(quantidade, 0, -1):
        if palavra[contador] == palavra[quantidade - 1]:
            contador = contador + 1
            quantidade = quantidade - 1
    if contador == len(palavra):
        print('é um palíndromo')
    else:
        print('não é um palíndromo')
else:
    print('não é um palíndromo.')

# CORREÇÃO
for ele in range(0, len(palavra)):
    if palavra[ele] == palavra[-ele-1]:
        compatibilidade = compatibilidade
if len(palavra) == compatibilidade:
    print('é um palíndromo')
else:
    print('não é um palíndromo')


# OU
if palavra == palavra[::-1]:
    print('é um palíndromo')
else:
    print('não é um palíndromo')










