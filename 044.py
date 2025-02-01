# Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
# Ao final deve mostrar a quantidade de vitórias
'''
import random
vitorias = 0
while True:
    escolha = input('Quer ser par ou impar? [P/I]: ').upper()
    numero = int(input('Digite o numero que deseja jogar: '))
    pc = random.randint(0, 10)
    if escolha == 'P':
        soma = numero + pc
        if soma % 2 == 0:
            print('voce ganhou!!')
        else:
            break
    elif escolha == 'I':
        soma = numero + pc
        if soma % 2 != 0:
            print('voce ganhou!!')
        else:
            break
    vitorias += 1
print(f'Você ganhou {vitorias} vezes!!')
'''


# Correção


import  random
try:
    vitorias = 0
    while True:
        pc = random.randint(0, 10)
        # Entradas usuario
        escolha = input((input('Digite'
                             '\n1 - Par'
                             '\n2 - Impar ->')))
        jogada = int(input('Qual a sua jogada? \n'))

        if ((pc + jogada) % 2 == 0 and escolha == 1) \
                or ((pc + jogada) % 2 == 1 and escolha == 2):
            print(f'Você Ganhou! A soma é {pc + jogada}')
        else:
            print(f'Você perdeu! A soma é {pc + jogada}')
            break
except ValueError:
    print('Apenas números inteiros.')


