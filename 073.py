# Crie uma classe Pessoa com atributos nome e idade. Adicione um método que exiba uma saudação.

class Pessoa:
    def __init__(self, nome, idade):
        try:
            if not isinstance(nome, str):
                raise TypeError('O nome deve ser uma string.')
            if not isinstance(idade, int) or idade < 0:
                raise ValueError('A idade deve ser um número inteiro positivo.')

            self.nome = nome
            self.idade = idade
        
        except(TypeError, ValueError) as e:
            print(f'Erro ao criar a pessoa: {e}')

    def saudacao(self):
        print(f'Olá, Meu nome é {self.nome}')
        