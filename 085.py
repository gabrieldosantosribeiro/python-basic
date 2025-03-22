# Crie uma classe Funcionario com atributos nome, salario e cargo. Adicione um método que calcule o bônus do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def calcularBonus(self):
        return self.salario * 0.10