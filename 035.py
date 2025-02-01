#Escreva um programa que leia o
#Nome, idade e sexo de 4 pessoas. No final mostre:
#A média de idade do grupo
#Qual é o homem mais velho
#Quantas mulheres têm menos de 20 anos
try:
    soma = 0
    maior = 0
    menor = 0
    for ele in range(0, 4):
        nome = input('qual seu nome: ')
        idade = int(input('digite sua idade: '))
        soma += idade
        sexo = input('qual se sexo[H / M]: ').lower()
        if sexo == 'h':
            if idade > maior:
                maior = idade
                MaisVelho = nome
        elif sexo == 'm':
            if idade < 20:
                menor += 1
    #média das idades
    print(f'a média das idades é {soma/4}')
    if maior > 0:
        print(f'o homem mais velho é {MaisVelho}')
    if menor > 1:
        print(f'{menor} mulheres tem menos de 20 anos')
    else:
        print(f'{menor} mulherer tem menos de 20 anos')
except ValueError:
    print('Apenas números inteiros.')


















