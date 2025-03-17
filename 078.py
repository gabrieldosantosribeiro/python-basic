# Crie uma classe Aluno com atributos nome e notas. Adicione um método que calcule a média das notas.

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionarNota(self, nota):
        self.notas.append(nota)

    def calcularMedia(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0