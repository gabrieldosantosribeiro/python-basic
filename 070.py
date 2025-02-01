# Escreva um programa que leia diversos alunos,
# crie um dicionário com as notas de dele em três disciplinas:
# matemática, português e história. Em seguida, exiba a média das notas do aluno.
todasnotas = {}
dicionario = {}
materias = ['Matemática', 'Português', 'História']

while True:
    nome = input('Digite seu nome[Fim]: ').strip().title()
    if nome == 'Fim':
        break
    for ele in materias:
        nota = input(f'Digite sua nota de {ele}: ')
        todasnotas[ele] = nota
        dicionario[nome] = todasnotas.copy()

for nome, notas in dicionario:
    print(f'A média de {nome} é, {sum(notas.values()) / len(notas.values())}')

'''
alunos  = {}

while True:
    nome = input('Digite o nome do aluno[Fim]: ').strip().title()
    if nome == 'Fim':
        break
    matematica = float(input('Digite sua nota de matematica: '))
    historia = float(input('Digite sua nota de historia: '))
    portugues = float(input('Digite sua nota de portugues: '))
    
    alunos[nome] = {'matematica': matematica, 'Historia': historia, 'Portugues': portugues}
     
for nome, notas in alunos.items():
    print(f'A média de {nome} é, {sum(notas.values()) / len(notas.values)}')

'''












'''
for ele in materias:
    nota = (float(input(f'"1" para sair'
                        f'\nDigite sua nota de {ele}: ')))
    dicionario[ele] = nota

for ele in dicionario:
    print(sum(dicionario[ele])/len(dicionario))
'''