# Crie uma classe Carro com atributos modelo, cor e ano. Adicione um método que exiba as informações do carro.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def exebir(self):
        print(f'Modelo: {self.modelo}\nCor: {self.cor}\nAno: {self.ano}')