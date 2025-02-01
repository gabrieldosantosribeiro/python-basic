#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
#V = (4/3) . π . r³
#A = 4 . π . r²
try:
    #variavel
    raio = float(input('digite o raio(m): '))
    volume = (4/3) * 3.14 * (raio ** 3)
    area = 4 * 3.14 * (raio ** 2)

    #retorno
    print(f'volume:  {volume:.2f} m³ \nárea: {area:.2f} m²')
except ValueError:
    print('O raio tem que ser um número.')