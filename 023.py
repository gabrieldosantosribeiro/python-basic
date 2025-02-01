#Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

palavra = input('digite uma palavra: ').strip().lower()

if palavra[0] in 'aeiou':
    print('a primeira letra é uma vogal')
else:
    print('a primeira letra é consoante')

