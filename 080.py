# Crie uma classe Biblioteca que gerencie uma coleção de livros. Adicione métodos para adicionar e remover livros.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False
    
    def devolver(self):
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)
        print(f"livro '{livro.titulo}' adicionado à biblioteca.")

    def emprestarLivro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.emprestar():
                print(f"livro '{titulo}' emprestado.")
                return
        print(f"livro '{titulo}' não disponível.")