#Crie um programa que pede ao usuário para digitar dois números e,
# em seguida, divida o primeiro número pelo segundo número.No entanto,
# o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido,
# como uma string ou o número zero.

#ZeroDivisionError ; ValueError
while True:
    try:
        numerador = int(input('Digite o numerador: '))
        denominador = int(input('Digite o denominador: '))
        print(f'O resultado da divisão é {numerador/denominador:.2f}')
    except ValueError:
        print('Só números inteiros!')
    except ZeroDivisionError:
        print('O denominador não pode ser 0!')





