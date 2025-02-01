#Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média,
# é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).
try:
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    nota3 = float(input('digite a terceira nota: '))
    nota4 = float(input('digite a quarta nota: '))
    nota5 = float(input('digite a quinta nota: '))

    media = (nota1 + nota2 + nota3 + nota4 + nota5)/5
    if media < 6:
        print('nota insuficiente')
    elif media >= 6 and media < 7:
        print('suficiente')
    elif media >= 7 and media < 9:
        print('bom')
    if media >= 9:
        print('exelente')
except ValueError:
    print('Precisa ser um número.')