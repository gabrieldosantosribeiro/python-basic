# Crie uma classe Jogo que tenha atributos nome, categoria e preco. Adicione um método que exiba informações sobre o jogo.

class Jogo:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
    
    def exibirInformacoes(self):
        print(f'Nome: {self.nome}\nCategoria: {self.categoria}\nPreço: {self.preco}')