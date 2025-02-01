# Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso

numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
          'Quatorze', 'Quinze')
try:
    posicao = int(input('Digite um número de 0 á 15: '))

    print(numero[posicao])
except ValueError:
    print('Apenas números inteiros.')
except IndexError:
    print('Apenas números de 0 a 15')






