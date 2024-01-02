#Importando biblioteca nativa do Python, para fazer implementações
import abc

class Pets(abc.ABC):
    def __init__(self):
        pass
    
    #Obriga que por padrão esse método seja definido em todas as classes herdeiras
    @abc.abstractmethod
    def sound(self):
        print(f'This animal makes a sound.')

class Dog(Pets):
    def __init__(self):
        pass

    def sound(self):
        print(f'The dog barks.')

class Cat(Pets):
    def __init__(self):
        pass

    def sound(self):
        print(f'The cat meows.')

if __name__ == '__main__':
    
    pets = [
        Dog(),
        Cat()
    ]
    
    for pet in pets:
        pet.sound()
