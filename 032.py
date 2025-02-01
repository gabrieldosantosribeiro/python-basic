#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.
try:
    n1 = int(input('digite o primeiro numero: '))
    n2 = int(input('digite o segundo numero: '))
    numeros = ''
    for ele in range(n1, n2 + 1):
        if ele % 2 == 0:
            numeros = numeros  + str(ele) + ', '
    print(numeros)
except ValueError:
    print('O programa só aceita números inteiros.')

