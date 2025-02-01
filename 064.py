# Crie um programa onde o usuário possa digitar sete letras,
# e cadastre em uma única lista, que mantenha separado as consoantes das vogais

lista = list()
consoantes = list()
vogais = list()

for ele in range(0, 7):
    palavra = input('digite uma letra: ').strip().lower()
    if palavra in 'aeiou:':
        vogais.append(palavra)
    else:
        consoantes.append(palavra)
lista.append(vogais[:])
lista.append(consoantes[:])
print(lista)





