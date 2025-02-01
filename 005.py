#Escreva um programa que converta real para o Franco Congolês
try:
    #variaveis
    real = float(input('digite o valor em reais: '))
    franco = real * 559.07

    # retorno
    print(f'equivale a {franco:.2f} francos congolês')
except ValueError:
    print('O valor de reais tem que ser um número.')


