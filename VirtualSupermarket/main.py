if __name__ == '__main__':
    # 1. Escrever um programa que recebe alguns produtos como argumento
    # 2. Validar se esses produtos estão na lista de itens disponíveis do mercado
    # 3. Caso estejam, avisar o usuário quais produtos têm e quais não têm
    # 4. Por último, exibir a lista de produtos disponíveis ordenados por ordem alfabética

    products_in_stock = ['Banana', 'Tomato', 'Milk', 'Broccoli', 'Eggs']
    wish_products = []
    available_products = []

    while True:
        product = input('Type the product you are looking for (enter 0 to finish): ')

        if product == '0':
            break

        else:
            wish_products.append(product)
            print(wish_products)

    print(f'Checking which of these items we have in stock...')

    for p in wish_products:
        if p in products_in_stock and p not in available_products:
            available_products.append(p)

    print(f'The following products are available: ')
    available_products.sort()
    print(available_products)