def wellcome(name):
    print(f'Wellcome {name}')


def wash_car(position):
    print(f'Washing car in position {position}...')


if __name__ == '__main__':
    # ESTRUTURAS DE REPETIÇÃO
    # For:
    for y in range(0, 3):
        print(f'The number is {y}')

    for n in range(0, 10, 2):
        print(f'The number is {n}')

    for letra in "palavra":
        print(letra)

    people = ['Luana', 'Vivian', 'Julian']

    for i, n in enumerate(people, start=0):
        print(f'{n} in position {i}')

    for n in people:
        wellcome(n)

    # While
    counter = 0

    while counter <= 3:
        wash_car(counter)
        counter += 1
    else:
        (f'All cars have been washed')
