#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10,
# entre 10 e 20 ou maior que 20.
try:
    # ler o numero
    numero = float(input('digite um numero: '))

    #conparação
    if numero > 0 and numero < 10:
        print('o numero está entre 0 e 10')
    elif numero > 10 and numero < 20:
        print('o numero está entre 10 e 20')
    elif numero > 20:
        print('o numero é maior que 20')
    else:
        print('menor que zero')
except ValueError:
    print('O valor digitado precisa ser um número.')