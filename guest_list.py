name = input('Enter your name: ')
age = int(input('Enter your age: '))

guest_list = ['Luana', 'Vivian', 'Anubis']
if age >= 18 and name in guest_list:
    print(f'{name}, you are able to enter the party')

else:
    print(f'You are not able to enter the party')
