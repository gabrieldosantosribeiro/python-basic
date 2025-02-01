#Crie um programa que verifica se uma pessoa pode ser doadora de sangue,
# considerando a idade e os critérios de saúde.

try:
    idade = int(input('informe sua idade: '))
    if idade > 16 and idade < 69:
        try:
            peso = float(input('informe seu peso: '))
            if peso > 50 and peso < 140:
                try:
                    sono = float(input('quantas horas você dormiu: '))
                    if sono > 6:
                        drogas = input('você é usuario de drogas: ').strip().lower()
                        if drogas == 'não':
                            gripe = input('você está gripado: ').strip().lower()
                            if gripe == 'não':
                                print('você pode doar!!!')
                            else:
                                print('você não pode doar')
                        else:
                            print('você não pode doar')
                    else:
                        print('você não pode doar')
                except ValueError:
                    print('Precisa ser um número.')
            else:
                print('você não pode doar')
        except ValueError:
            print('O peso precisa ser um número.')
    else:
        print('você não pode doar')
except ValueError:
    print('A idade precisa ser um número inteiro.')


