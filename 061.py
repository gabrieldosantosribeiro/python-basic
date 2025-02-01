# Escreva um programa que crie uma lista vazia e permita que
# o usuário insira números nessa lista até que ele digite um número negativo.
# Em seguida, exiba a lista na tela.

try:
    lista = []
    while True:
        numero = float(input('Digite um número: '))
        if numero > 0:
            lista.append(numero)
        else:
            print(lista)
            break
except ValueError:
    print('O programa só aceita números.')



