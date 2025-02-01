# Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista.
# No final mostre:
#
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas com o maior QI
# Uma listagem com as pessoas de menor QI
try:
    lista = list()
    nomes = list()
    qi = list()
    parar = None
    while parar != 'S':
        nomes.append(input('Digite seu nome: '))
        qi.append(int(input('Digite seu QI: ')))
        parar = input('Deseja parar?[S/N] ').upper()
    lista.append(nomes[:])
    lista.append(qi[:])


    print(f'O total de pessoas cadastradas foi: {len(lista)}\n'
          f'Os maiores QI são: {sorted(lista[1], reverse=True)[:(len(lista[1])//2)]} \n'
          f'Os menores QI são: {sorted(lista[1])[:(len(lista[1])//2)]}')
except ValueError:
    print('Apenas números. ')

