#Escreva um programa que leia uma frase,
# e mostre uma formatação adaptável de acordo com o tamanho da frase,
# coordenado por uma função

#Exemplo:
#       ----------------------------
#            Senai Show de bola
#       ----------------------------
'''
def formatar(frase):
    print('----', end= '')
    print('-' * len(frase))
    print(' ' , frase)
    print('----', end= '')
    print('-' * len(frase))




frase = input('Digite a frase: ').strip()
formatar(frase)

'''


def frase_bonita(msg):
    tamanho = len(msg)
    print('--' * tamanho)
    print(f'{msg.center(2 * (tamanho))}')
    print('--' * tamanho)

frase_bonita('SENAI SUZANO')



