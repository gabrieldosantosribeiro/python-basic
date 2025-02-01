# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta

lista = []
exp = input('Digite algo: ')
try:
    # Separar as letras em uma lista
    for ele in exp:
        for letra in ele:
            lista.append(letra)
    # loop até o final
    while True:
        # Achar o primeiro parênteses aberto
        aberto = int((lista.index('(')))
        # Achar o primeiro parênteses fechado
        fechado = int((lista.index(')')))

        # Comparar
        if fechado > aberto:
            lista.pop(fechado)
            lista.pop(aberto)
            if len(lista) == 0 or len(lista) % 2 != 0:
                break
        else:
            break
    if len(lista) > 0:
        print('Errado')
    else:
        print('Certo')
except ValueError:
    print('Errado')



