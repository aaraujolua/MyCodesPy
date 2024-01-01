#Conceitos de herança
class  Animal:
    def __init__ (self,name, weight):
        self.name = name
        self.weight = weight
        
    def breathe (self):
        print(f'The {self.name} is breathing. Its size is {self.weight}m.')
        

class Mammal (Animal):
    def __init__ (self, name, weight):
        super().__init__(name, weight)
        
    def breastfeed (self):
        print(f'The {self.name} is breastfeeding.')
    
    
class Reptile (Animal):
    def __init__ (self, name, weight):
        super().__init__(name, weight)
        
    def layEgg (self):
        print(f'The {self.name} is laying an egg.')
        

if __name__ == '__main__':
    
    animal1 = Mammal('Cow', 720)
    animal2 = Reptile('Crocodile', 1000 )
    
    animal1.breathe()
    animal2.breathe()