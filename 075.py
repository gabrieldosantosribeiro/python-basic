# Crie uma classe Animal com um método falar que retorne um som genérico. Crie subclasses para Cachorro e Gato que sobrescrevam o método falar.

class Animal:
    def falar(self):
        return 'som genérico'
    
class Cachorro(Animal):
    def falar(self):
        return 'au au'
    
class Gato(Animal):
    def falar(self):
        return 'miau'