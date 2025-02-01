#Crie um programa que leia um nome, e mostre o primeiro e o último nome

#ler o nome
nome = input('digite um nome: ').strip().split()
#primeiro nome
print(nome[0])
#ultimo nome
ultimo = (len(nome)- 1)
print(nome[ultimo])


