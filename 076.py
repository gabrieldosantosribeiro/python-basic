# Crie uma classe ContaBancaria com atributos titular e saldo. Adicione métodos para depositar e sacar dinheiro.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'deposito de {valor} realizado.')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'saque de {valor} realizado.')
        else:
            print('saldo insuficiente.')
    
    def exibir(self):
        return f'saldo atual: {self.saldo}'