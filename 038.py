#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
#1.	Somar
#2.	Multiplicar
#3.	Maior
#4.	Novos números
#5.	Sair do programa
try:
    num1 = float(input('digite o primeiro numero: '))
    num2 = float(input('digite o segundo numero: '))
    num3 = float(input('digite o terceiro numero: '))
    resposta = None
    while resposta != 5:
        try:
            escolha = int(input('1. somar'
                            '\n2. multiplicar'
                            '\n3. maior'
                            '\n4. novos numeros'
                            '\n5. sair do programa'
                            '\nDigite sua escolha: '))
            if escolha == 1:
                print(f'a soma dos números é {num1 + num2 + num3}')
            elif escolha == 2:
                print(f'o produto dos números é {num1 * num2 * num3}')
            elif escolha == 3:
                if num1 < num2:
                    if num2 > num3:
                        print(f'{num2} é o maior numero')
                    else:
                        print(f'{num3} é o maior numero')
                elif num1 > num3:
                    print(f'{num1} é o maior numero')
                else:
                    print(f'{num3} é o maior numero')
            elif escolha == 4:
                num1 = float(input('digite o primeiro numero: '))
                num2 = float(input('digite o segundo numero: '))
                num3 = float(input('digite o terceiro numero: '))
            elif escolha == 5:
                resposta = None
            else:
                print('Apenas números indicados.')
        except ValueError:
            print('Apenas os números indicados')
except ValueError:
    print('Apenas números.')










