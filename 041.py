# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
soma = 0
contador = 0
maior = None
menor = None
parar = None
try:
    while parar != 'N':
        contador += 1
        numero = int(input('Digite um número: '))
        soma += numero
        if contador == 1:
            menor = numero
            maior = numero
        elif numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
        parar = input('Deseja continuar? [S/N] ').upper()
    print(f'a média dos números é {soma/contador:.2f}'
          f'\no maior número digitado foi {maior}'
          f'\no menor numero digitado foi {menor}')
except ValueError:
    print('Apenas números inteiros.')










