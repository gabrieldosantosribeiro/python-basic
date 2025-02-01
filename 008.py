#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.
try:
    #variaveis
    salario = float(input('digite seu salário: '))
    reajuste = salario + salario * 0.6

    #retorno
    print(f'o salario reajustado é {salario * 1.6}')
except ValueError:
    print('O salário precisa ser um número.')
