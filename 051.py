#Crie uma função para verificar se um número é par ou ímpar
try:
    def parimpar(numero):
        if numero % 2 == 0:
            return('O número é par!!')
        else:
            return('O número é impar!!')


    numero = int(input('Digite um número: '))
    print(parimpar(numero))
except ValueError:
    print('Só digite números inteiros')

