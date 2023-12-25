n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

op = input('Which operation you want to do (+,-,*,/)? ')

if op == '+':
    print(f'The result is', n1 + n2)

elif op == '-':
    print(f'The result is', n1 - n2)

elif op == '*':
    print(f'The result is', n1 * n2)

elif op == '/':
    print(f'The result is', n1 / n2)

else:
    print(f'Choose a valid operation')