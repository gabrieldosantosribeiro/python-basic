# Crie uma classe Professor que herde de Pessoa e adicione um atributo disciplina e um método que exiba informações sobre o professor.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    
    def informacoes(self):
        return f'Professor(a): {self.nome}\nIdade: {self.idade}\nDisciplina: {self.disciplina}'