#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário
try:
    #variaveis
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    cidade = input('Digite sua cidade de nascimento: ')

    #retornar para o usuário
    print(f'O seu nome é {nome}, sua idade é {idade} e você nasceu em {cidade}')
except ValueError:
    print('Sue idade precisa ser um número inteiro.')
