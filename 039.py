#Faça um programa que leia um número e retorne o fatorial !
#4! = 4 x 3 x 2 x 1
try:
    numero = int(input('Digite um número: '))
    contador = 1
    fatorial = 1
    while contador != numero:
        contador += 1
        fatorial = contador * fatorial

    print(fatorial)
except ValueError:
    print('Apenas números inteiros.')