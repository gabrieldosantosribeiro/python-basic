# Crie um programa para analisar o IMC de uma pessoa,
# e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.
try:
    peso = float(input('informe seu peso: '))
    altura = float(input('informe sua altura: '))

    imc = peso / (altura ** 2)
    print(imc)
    if imc >= 18.5 and imc <= 24.9:
        print('faixa ideal')
    elif imc < 18.5:
        print('abaixo')
    else:
        print('acima')
except ValueError:
    print('O valor precisa ser um número..')
