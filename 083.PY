# Desenvolva um sistema de gerenciamento de tarefas com as classes Tarefa e Usuario, incluindo métodos para adicionar tarefas, marcar como concluídas e listar tarefas com seus respectivos status.

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False
    
    def concluir(self):
        self.concluida = True
    
    def __str__(self):
        status = 'conculida' if self.concluida else 'pendente'
        return f'tarefa: {self.descricao} - status: {status}'

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
    
    def adicionarTarefa(self, tarefa):
        self.tarefas.append(tarefa)
    
    def listarTarefas(self):
        print(f'tarefas de {self.nome}:')
        for tarefa in self.tarefas:
            print(tarefa)