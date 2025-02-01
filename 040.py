#Escreva um programa que leia um número n inteiro qualquer
# e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci
'''
numero = int(input('Digite um número: '))
contagem = 0
a1 = 0
a2 = 1
if numero > 0:
    if numero == 1:
        print('0')
    elif numero == 2:
        print('0 1')
    else:
        contagem = 2
        while contagem < numero:
            if contagem < 3:
                print('0 1', end= ' ')
            contagem += 1
            fibonacci = a1 + a2
            a2 = fibonacci
            a1 = fibonacci - a1
            print(fibonacci, end= ' ')
'''
try:
    n = int(input('Quantos ? '))
    ciclo = 0
    prox = 0
    atual = 1
    anterior = 0
    while ciclo < n:
        if ciclo == 0:
            print('0')
        elif ciclo == 1:
            print('1')
        else:
            prox = atual + anterior
            anterior = atual
            atual = prox
            print(prox)

        ciclo += 1
except ValueError:
    print('Apenas números inteiros.')













