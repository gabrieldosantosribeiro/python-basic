# Faça um programa com uma função maior e menor,
# que leia uma lista com 5 valores informados pelo usuário
# e retorne esses valores e a posição deles
try:
    lista = []
    for ele in range(0, 5):
        valor = float(input('Digite um valor: '))
        lista.append(valor)
    for pos, valor in enumerate(lista):
        print(f'Posição {pos}: {valor}')
except ValueError:
    print('O programa só aceita números. ')






