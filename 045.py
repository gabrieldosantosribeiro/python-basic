# Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000

while True:
    numero = input('digite um numero: ')
    if numero == '0000':
        break
    else:
        for ele in range(0, 11):
            print(f'{numero} x {ele} = {int(numero) * ele}')





