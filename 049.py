#Crie um programa que tenha a função área(),
# que receba as dimensões de um muro retangular e mostra a área do terreno

def area(primeiro, segundo):
    area = primeiro * segundo
    return area

primeiro = float(input('Digite o tamanho do primeiro muro: '))
segundo = float(input('Digite o tamanho do segundo muro: '))

area = area(primeiro, segundo)
print(area)


