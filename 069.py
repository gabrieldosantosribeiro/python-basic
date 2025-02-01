# Escreva um programa que crie um dicionário com os nomes e preços de 5 produtos.
# Em seguida, exiba o produto mais barato e o mais caro.
'''
nomes = list()
valores = list()
for ele in range(2):
    nome = input('Digite o produto: ')
    valor = float(input('Digite o preço: '))
    valores.append(valor)
    nomes.append(nome)

#(valores.index(max(valores)))
#(valores.index(min(valores)))
print(f'O produto mais barato é: {nomes[valores.index(min(valores))]}'
      f'\nO produto mais caro é: {nomes[valores.index(max(valores))]}')
'''
try:
    produtos = {}
    for ele in range(3):
        nome = input('Digite o produto: ')
        valor = float(input('Digite o valor: '))  # float
        produtos[nome] = valor

    '''  
    maior = None
    chave_maior = None
    menor = None
    chave_menor = None
    
    for chave, valor in produtos.items():
        if maior == None:
            maior = valor
            chave_maior = chave
            menor = valor
            chave_menor = chave
        if valor > maior:
            maior = valor
            chave_maior = chave
        if valor < menor:
            menor = valor
            chave_menor = chave
    '''

    maior = max(produtos.values())
    menor = min(produtos.values())

    for ele in produtos:
        print(produtos[ele])
        if ele == maior:
            maior = produtos[ele]
        elif ele == menor:
            menor = produtos[ele]

    print(f'O produto mais caro é: {maior}'
          f'\nO produto mais barato é: {menor}')



except ValueError:
    print('Apenas números.')




