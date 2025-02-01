#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

# Ler o numero
numero = float(input('digite um numero: '))
# Comparação
if numero % 2 == 0:
    print('o numero é par')
else:
    print('o numero é impar')