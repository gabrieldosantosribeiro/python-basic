#Escreva um programa que leia 6 notas diferentes e faça a média do aluno
try:
    #variaveis
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    nota3 = float(input('digite a terceira nota: '))
    nota4 = float(input('digite a quarta nota: '))
    nota5 = float(input('digite a quinta nota: '))
    nota6 = float(input('digite a sexta nota: '))

    media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6) / 6

    #retorno
    print(f'A média é{media}')
except ValueError:
    print('A nota não pode ser uma letra.')

