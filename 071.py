# Crie um programa que leia
# nome,ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário,
# se por acaso a Carteira de trabalho for diferente de zero.
# O Dicionário receberá também o ano de contratação e o saláro.
# Calcule e apresente, além da idade, com quantos anos a pessoa vai se aposentar

dicionario = {}
while True:
    try:
        dicionario['Nome'] = input('Digite seu nome: ')
        dicionario['Ano de nascimento'] = int(input('Digite seu ano de nascimento: '))
        carteira = input('Tem carteira de trabalho? [S/N] ').upper()
        if carteira == 'S':
            dicionario['Ano de contratação'] = int(input('Digite o ano de contratação: '))
            dicionario['Salário'] = float(input('Digite seu salário: '))
            print(f'Sua idade é: {2024 - dicionario["Ano de nascimento"]}'
                  f'\nVai aposentar com {(dicionario["Ano de contratação"] + 30) - dicionario["Ano de nascimento"]} '
                  f'anos.')
        elif carteira == 'N':
            print(f'Sua idade é: {2024 - dicionario["Ano de nascimento"]}')
        else:
            print('Apenas [S/N]. ')
    except ValueError:
        print('Apenas números.')
