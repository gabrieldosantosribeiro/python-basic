# Crie um programa que leia o nome, sexo e idade de vários Alunos, guardando os dados de cada aluno em um dicionário
# e todos os dicionários em uma lista. No final mostre:
#
# 1. Quantas pessoas foram cadastradas
# 2. A média de idade do grupo
# 3. Uma lista com todas as mulheres
# 4. Uma lista com todas as pessoas com idade acima da média
while True:
    try:
        lista = list()
        mulheres = list()
        # Cadastro
        dicionario = {}
        dicionario['Nome'] = input('"1" para encerrar. Digite seu nome: ')
        # Parar
        if dicionario['Nome'] == '1':
            break
        else:
            dicionario['Sexo'] = input('Digite seu sexo: [M/F] ').upper()
            dicionario['Idade'] = int(input('Digite sua idade: '))
            lista.append(dicionario.copy())
            if dicionario['Sexo'] == 'F':
                mulheres.append(dicionario['Nome'])
            dicionario.clear()
            print(lista)

            # Acima da média
            acima = list()
            for ele in lista:
                if ele['Idade'] > (sum(ele['Idade'] for ele in lista)) / len(lista):
                    acima.append(ele['Nome'])

            # Mostrar
            print(f'O total de pessoas cadastradas é: {len(lista)}'
                  f'\nA média de idade do grupo é: {(sum(ele["Idade"] for ele in lista)) / len(lista)}'
                  f'\nA lista de mulheres cadastradas: {mulheres}'
                  f'\nA lista de pessoas com idade acima da média: {acima}')
    except ValueError:
        print('Apenas números inteiros.')
