#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas as letras maiúsculas
#-O nome com todas minúsculas
#-Quantas letras ao todo (sem considerar os espaços)
#-Quantas letras tem o primeiro nome

#ler o nome
nome = input('digite seu nome completo: ').strip()
#mostrar para o usuario
print(nome.upper())
print(nome.lower())
letras = nome.replace(' ', '')
print(len(letras))
nome_separado = nome.split()
print(len(nome_separado[0]))
