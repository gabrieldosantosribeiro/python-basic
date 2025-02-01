#Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos).
try:
    # Ler idade
    idade = int(input('digite sua idade: '))

    #comparação
    if idade > 18:
        print('você é maior de idade')
    else:
        print('você é menor de idade')
except ValueError:
    print('A idade precisa ser um número inteiro.')

