#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random
import time

#variaveis
pedra = 1
papel = 2
tesoura = 3
try:
    jogador = (int(input('o numero 1 é pedra'
                    '\no numero 2 é papel'
                    '\no numero 3 é tesoura'
                    '\n'
                    '\n digite sua escolha: ')))
    if jogador <= 3 and jogador >= 1:
        time.sleep(0.5)
        print('Jo')
        time.sleep(0.5)
        print('Kem')
        time.sleep(0.5)
        print('Po')

        pc = (random.randint(1, 3))
        print(pc)
        if pc != jogador:
            if pc == 1 and jogador == 2:
                print('você ganhou')
            elif pc == 1 and jogador == 3:
                print('você perdeu')
            elif pc == 2 and jogador == 1:
                print('você perdeu')
            elif pc == 2 and jogador == 3:
                print('você ganhou')
            elif pc == 3 and jogador == 1:
                print('você ganhou')
            elif pc == 3 and jogador == 2:
                print('você perdeu')
        else:
            print('empate')
    else:
        print('O número precisa ser de 1 até 3')

except ValueError:
    print('A escolha precisa ser um número inteiro.')



