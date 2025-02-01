# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:

# 1. Qual é o total gasto na compra
# 2. Quantos produtos custam mais de R$1000,00
# 3. Qual é o produto mais barato
try:
    maior = 0
    menor = None
    total = 0
    while True:
        preco = float(input('Digite o valor do produto: '))
        if total == 0:
            menor = preco
        total += preco
        if preco > 1000:
            maior += 1
        if preco < menor:
            menor = preco
        continuar = input('Deseja continuar? [S/N]').upper()
        if continuar == 'N':
            break
    print(f'O total de gastos foi {total} reais'
          f'\n{maior} produtos custaram mais de 1000 reais'
          f'\no prosuto mais barato custou {menor} reais')
except ValueError:
    print('Apenas números.')




