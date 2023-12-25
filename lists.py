animals = ['Monkey', 'Bear', 'Cat']
print(animals)

animals.append('Aligator') #Adiciona um elemento no final da lista
print(animals)

animals.insert(1, 'Whale') #Insere um elemento na posição desejada
print(animals)

animals.remove('Whale') #Remove o elemento
animals.insert(2, 'Flamingo')
print(animals)

animals.sort() #Lista de acordo com o parâmetro que vc der (default: ordem alfabética)
print(animals)

number_animal = animals.count('Flamingo') #Mostra quantos Flamingos tem na lista
print(number_animal)

numberAnimals = len(animals)
print(numberAnimals)

animals.clear() #Limpa a lista
print(animals)