'''
# Operações com python
print(1 + 1)
print(1024 * 152)
print(1024 / 2)
print(8 ** 2)

print('Bem vindo ao curso de Python')

# Variáveis
a = 1
b = 2
c = a + b
print(c)

# Print formatado
idade = 45
print(f'A sua idade è {idade} ')


# Leitura de Variável // input para declarar a variavél
nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
print(f'Seu nome é {nome} e sua idade é {idade}')


# float e int
idade1 = float(input('digite sua idade: '))
idade2 = int(input('digite outra idade: '))

soma = idade1 + idade2

print(f'A soma é {soma}')

print(type(1))
print(type('oi'))
print(type(5.10))

dado = '1'
print(dado.isalpha())


Senai = 'Luis eulalio'
#Fatiar
print(Senai[0])
print(Senai[0:7])
#Cortar
print(len(Senai))
print(Senai.count('L'))
#Formataçã
Senai = Senai.replace('l', 'A')
print(Senai)
print(Senai.upper())
print(Senai.lower())
Nome = input('digite seu nome: ').strip()
print(Nome)
print(len(Nome))

Nome = input('digite seu nome: ').strip()
Nome_separado = Nome.split()
print(Nome_separado)


altura = float(input('digite a sua altura: '))

#caso simples
if altura > 1.2:
    print('voce pode andar no brinquedo')
else:
    print('quem sabe ano que vem')

#caso composto
if altura < 1.2:
    print('quem sabe ano que vem')
elif altura > 3:
    print('voce é muito alto!!')
else:
    print('voce pode andar')

nome = 'Luis Tatin'
if nome == 'Luis Tatin':
    print('Bem vindo')
else:
    print('nome incorreto')

import random

aleatorio = random.randint(1, 3)

# simples
for ele in range(0, 10):
    print('*')

#variavel auxiliar
soma = 0
for ele in range(0, 10):
    numero = int(input('digite um numero: '))
    soma = soma + numero

print(f'{soma}')


#negativo
for ele in range(10, 0, -1):
    print('negativo')


contador = 0

while contador <5:
    print('oi')
    contador += 1


# String
resposta = ''
while resposta != 'N':
    print('oi')
    resposta = input('deseja continuar? [S/N]').upper()


lista = []

lista.append('oi')
lista.insert(0, 'olá')
lista.append(3)
print(lista)



lista = ['1', '2', '3']

ele = 0
for ele in range(0, len(lista)):
    if lista[ele] == '2':
        print(f'A posicao é {ele}')

while True:
    try:
        numero = int(input('Digite sua idade: '))
        x = 10 / 0

    except ValueError:
        print('Só aceitamos números')
    except:
        print('Erro')

isinstance(objeto, tipo) # verifica se um objeto é de um tipo específico

raise # palavra chave para lançar uma exceção manualmente (interrompe o código e 'avisa' o erro)
# sintaxe
raise Excecao("Mensagem de erro")

def mostrar_linha():
    print('-*-' * 30)

mostrar_linha()

def mensagem_personalizada(msg):
    print('-------')
    print(msg)
    print('-------')

mensagem_personalizada('Bem vindo')

def quadrado(n):
    resultado = n ** 2
    return resultado


carro = ('Ferrari', 'Vermelha', '2023')
print(carro)

for ele in carro:
    print(ele)

for count in range(0, len(carro)):
    print(carro[count])

for pos, carac in enumerate(carro):
    print(f'Ordem de compra {carac} Cod: {pos}')

# Parte 1

danilo = (1, 2, 3)
daniel = (5, 6, 7, 8)
c = danilo + daniel

print(c)

print(c.index(3))

# Parte 2
del(c)

# Mutáveis
# Representadas por []


carro = ['Ferrari', 'Vermelha', '2023']
carro [1] = 'Amarelo'
carro.append('Gasolina')     # cria no final da lista
carro.insert(1, '797 cv ')   # insere na posição 1
carro.pop(1)                 # remove o item na posição 1
carro.remove('Vermelha')     # remove o valor 'vermelha'
len(carro)                   # retorna o tamanho da lista



idades = [1,2,3,6,3,25,6,89,3,6,9,]
print(sum(idades))
print(max(idades))
print(min(idades))
print(sum(idades)/len(idades))


ListaIdades = [1, 2, 3, 4, 5]
ListaNomes = ['Felipe', 'João', 'Matheus', 'Marcos', 'Agostinho']
print(ListaIdades)
print(ListaNomes)
ListaCadastro = []
ListaCadastro.append(ListaIdades[:])
ListaCadastro.append(ListaNomes[:])
print(ListaCadastro)
print(ListaCadastro[0][0])
print(ListaCadastro[1][0])
print(sum(ListaCadastro[0]))



funcionario = {'nome': 'Luis', 'idade': 23}
print(funcionario['nome'])
funcionarios = {'nomes': ['Luis Tstin','a','b','c'], 'idades': [23,1,2,3]}
print(funcionarios['nomes'[2]])

for ele in funcionarios['idades']:
    print(ele)

pessoa = {}
chave = input('Digite a chave: ')
valor = input('Digite o valor: ')

pessoa[chave] = valor

print(pessoa)



def dobro(numero):
    resultado = numero * 2
    return resultado


num = float(input('Digite: '))
print(dobro(num))


# cria uma classe
class NomeDaClasse:
    pass
    
# herança - a subclasse herda atributos e métodos da superclasse
class Animal:
    def falar(self):
        print('som de animal')

class Cachorro(Animal): # Cachorro herda de Animal
    def falar(self): # sobrescreve o método da superclasse
        print('au au')

# polimorfismo - métodos com o mesmo nome, mas comportamentos diferente
class Gato(Animal):
    def falar(self):
        print('miau')

# super() - chama métodos ou o construtor da superclasse
class Veiculo:
    def __init__(self, modelo):
        self.modelo = modelo

class Carro(Veiculo):
    def __init__(self, modelo, cor):
        super().__init__(modelo) # chama o construtor de Veiculo
        self.cor = cor
'''