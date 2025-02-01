#Escreva um programa que peça ao usuário um número de 1 a 7
# e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).
try:
    numero = int(input('digite um numero de 1 a 7: '))

    if numero >= 1 and numero <= 7:
        if numero == 1:
            print('segunda-feira')
        elif numero == 2:
            print('terça-feira')
        elif numero == 3:
            print('quarta-feira')
        elif numero == 4:
            print('quinta-feira')
        elif numero == 5:
            print('sexta-feira')
        elif numero == 6:
            print('sabado')
        elif numero == 7:
            print('domingo')
    else:
        print('O número tem que ser de 1 até 7.')
except ValueError:
    print('Precisa ser um número inteiro.')
