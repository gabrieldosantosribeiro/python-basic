#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.
try:
    # ler os numeros
    numero1 = float(input('digite o primeiro numero: '))
    numero2 = float(input('digite o segundo numero: '))
    # Comparação
    if numero1 == numero2:
         print('os numeros são iguais')
    else:
        print('os numeros são diferentes')
except ValueError:
    print('O valor precisa ser um número.')