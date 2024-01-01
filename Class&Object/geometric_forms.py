#Conceitos de polimorfismo
class GeometricForms:
    def __init__(self):
        pass
    
    def draw(self):
        print(f'You are drawing a geometric form.')
        

class Circle(GeometricForms):
    def __init_ (self):
        pass


class Square(GeometricForms):
    def __init_ (self):
        pass
    
    #Sobrescrevendo o método da classe pai
    def draw(self):
        print(f'You are drawing a square.')
        
if __name__ == '__main__':
    
    forms = [
        Circle(),
        Square()
    ]
    
    for form in forms:
        form.draw()