#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
try:
    numero = int(input('digite um numero: '))

    for ele in range(0, 11):
        print(f'{numero} x {ele} = {numero * ele}')
except ValueError:
    print('O programa aceita apenas números.')