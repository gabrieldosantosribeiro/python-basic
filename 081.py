# Implemente um sistema de login com classes Usuario e SistemaAutenticacao. Adicione métodos para registrar e autenticar usuários.

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

class SistemaAutenticacao:
    def __init__(self):
        self.usuarios = []

    def registrar(self, nome, senha):
        if any(usuario.nome == nome for usuario in self.usuarios):
            print(f'usuario: {nome} ja existe.')
            return False
        usuario = Usuario(nome, senha)
        self.usuarios.append(usuario)
        print(f'usuario {nome} registrado com sucesso!')
        return True
    
    def autenticar(self, nome, senha):
        for usuario in self.usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                print(f'usuario {nome} autenticado com sucesso!')
                return True
        print(f'usuario ou senha inválidos.')
        return False