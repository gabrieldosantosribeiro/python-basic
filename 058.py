# Crie um programa onde serão informados diversos valores em uma lista.
# Caso o número já exista ele não será adicionado.
# No final, serão exibidos todos os valores únicos em ordem crescente
try:
    lista = []
    continuar = 'S'
    while continuar == 'S':
        valor = float(input('Digite um valor: '))
        if valor not in lista:
            lista.append(valor)
        continuar = input('Deseja continuar? [S/N]: ').upper()
    print(lista)
except ValueError:
    print('O programa só aceita números. ')












