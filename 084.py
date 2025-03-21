# Implemente uma classe CarrinhoDeCompras que armazene produtos e tenha métodos para adicionar, remover e calcular o total.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.carrinho = []
    
    def adicionarProduto(self, produto):
        self.carrinho.append(produto)
    
    def removerProduto(self, produto):
        self.carrinho.remove(produto)
    
    def calcularTotal(self):
        total = 0
        for produto in self.carrinho:
            total += produto.preco
        print(f'o total do carrinho é: {total}')