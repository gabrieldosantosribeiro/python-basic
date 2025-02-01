#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.
try:
    # Ler o numero
    numero = float(input('digite um numero: '))
    # comparação
    if numero > 0:
        print('o numero é positivo')
    else:
        print('o numero é negativo')
except ValueError:
    print('Digite apenas número.')