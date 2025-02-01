# Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico,
# permitindo que o usuário faça depósitos, saques e consulte o saldo da conta, e sair
saldo = 0
escolha = None
while escolha != 4:
    try:
        escolha = int(input('\nO que deseja fazer?'
                             '\n1. Depositar'
                             '\n2. Sacar'
                             '\n3. Consultar Saldo'
                             '\n4. Sair'
                             '\n'
                             '\nDigite aqui: '))
        try:
            if escolha < 0 or escolha > 4:
                print('Apenas números inteiros.')
            else:
                if escolha == 1:
                    deposito = float(input('\nQuanto você deseja depositar? \n'))
                    if deposito > 0:
                        saldo += deposito
                    else:
                        print('Operação invalida.')
                elif escolha == 2:
                    saque = float(input('\nQuanto você deseja sacar? \n'))
                    if saque > 0:
                        if saque < saldo:
                            saldo -= saque
                        else:
                            print('\nSaldo insuficiente.')
                    else:
                        print('Operação invalida.')
                elif escolha == 3:
                    print(f'\nO seu saldo é: {saldo}')
        except ValueError:
            print('Apenas números.')
    except ValueError:
        print('Apenas números inteiros.')






