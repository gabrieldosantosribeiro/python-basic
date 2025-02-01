#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
try:
    #variaveis
    n1 = float(input('digite um numero: '))
    dobro = n1 * 2
    triplo = n1 * 3
    raiz =  n1 ** (1/2)

    #retorno
    print(f'o dobro é {dobro}, o triplo é {triplo}e a raiz quadrada é {raiz}')
except ValueError:
    print('Precisa ser um número.')
