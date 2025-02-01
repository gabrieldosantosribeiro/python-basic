#Crie um programa que leia vários números inteiros.
# O programa só vai parar quando o usuário digitar 0000.
# No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)
'''
contagem = 0
soma = 0
while True:
    num = int(input('Digite um numero: '))
    contagem += 1
    soma += num
    parar = input('Deseja parar? se sim digite "0000": ')
    if parar == '0000':
        print(f'O total de numeros digitados foi {contagem} e a soma entre eles é {soma}')
        break
'''
try:
    soma= 0
    contagem = 0
    while True:
        numero = input('Digite um numero: ')
        if numero == '0000':
            break

        soma += int(numero)
        contagem += 1
    print(f'A soma é {soma}\n o total de numeros digitados foi {contagem}')
except ValueError:
    print('Apenas números.')




