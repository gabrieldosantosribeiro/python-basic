#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
# o programa vai informar quantas cédulas de cada valor serão entregues.

#Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

try:
    saque = int(input('---Caixa eletrônico---'
                        '\nQual será o valor sacado?'
                        '\n'))
    quant50 = 0
    while saque - 50 >= 0:
        quant50 += 1
        saque -= 50

    quant20 = 0
    while saque - 20 >= 0:
        quant20 += 1
        saque -= 20

    quant10 = 0
    while saque - 10 >= 0:
        quant10 += 1
        saque -= 10

    quant1 = 0
    while saque - 1 >= 0:
        quant1 += 1
        saque -= 1

    print(f'A quantidade de notas que serão entregues é:'
          f'\nR$50 é {quant50}'
          f'\nR$20 é {quant20}'
          f'\nR$10 é {quant10}'
          f'\nR$1 é {quant1}')
except ValueError:
    print('Apenas números inteiros.')





