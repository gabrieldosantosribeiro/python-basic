#Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma
try:
    soma = 0
    for ele in range(0, 10):
        numero = int(input('digite um número: '))
        if numero % 2 == 0:
            soma = soma + numero
    print(soma)
except ValueError:
    print('O programa só aceita números inteiros.')




