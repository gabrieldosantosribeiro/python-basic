#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
'''
maior = None
menor = None
'''
try:
    for ele in range(0, 7):
        peso = float(input('digite seu peso: '))
        '''
        if maior == None and menor == None:
            menor = peso
            maior = peso
            '''
        if ele == 1:
            maior = peso
            menor = peso
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    print(f'o menor peso é {menor}')
    print(f'o maior peso é {maior}')
except ValueError:
    print('Apenas números.')


