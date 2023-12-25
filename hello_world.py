def hello_world(name):
    print(f'Hello world, my name is {name}')

    print(f'Second comand')

# Exemplo de função
def validation(valid):
    if valid == True:
        return 'OK'

    else:
        return 'It is not valid'

if __name__ == '__main__':
    hello_world('Luana')

    name = 'James'
    print (type(name))
    name = 123
    print (type(name))

    names = ['Luana', 'James', 'Bob']
    print (names[0], 'and', names[1])

    person_data = {
        "name": "Luana",
        "age": 18,
        "country": "Brasil"
    }
    print (person_data['age'])
    print (type(person_data))

# Exemplo de comando de entrada
    name = input('Enter your name: ')
    print (f'Your name is {name}')

    n1 = int(input('Enter the first number: '))
    n2 = int(input('Enter the second number: '))
    sum = n1 + n2
    print (f'The sum of these two numbers is {sum}')

    # OPERADORES BINÁRIOS
    def second_operator():
        print(f'Assessing second operator...')
        return True
    # And
    a = False and second_operator()
    print(a)

    # Or
    b = False or second_operator()
    print(b)

    #ESTRUTURAS DE SELEÇÃO

    name = input('Enter a name: ')

    if name == 'Luana':
        print (f'The name is Luana')

    elif name == 'Bob':
        print (f'The name is Bob')

    else:
        print(f'This name is not in the list')

    test = False

    print(validation(test))