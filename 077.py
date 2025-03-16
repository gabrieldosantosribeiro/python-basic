# Crie uma classe Produto com atributos nome, preco e quantidade. Adicione um método que calcule o valor total em estoque.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def valorTotalEstoque(self):
        return self.preco * self.quantidade