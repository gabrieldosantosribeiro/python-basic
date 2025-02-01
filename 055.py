# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois, deve mostrar para cada palavra, suas vogais

palavras = ('Caderno', 'Lapis', 'Borracha', 'Caneta', 'Folha')

for ele in palavras:
    print(ele, end= ': ')
    for letra in ele:
        if letra in 'aeiou':
            print(letra, end= '')
    print(' ', end= '\n')






