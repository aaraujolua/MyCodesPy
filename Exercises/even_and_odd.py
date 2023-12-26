if __name__ == '__main__':
    even = []
    odd = []
    
    for i in range(0,21):
        if i % 2 == 0:
           even.append(i)
        else:
            odd.append(i)
    
    even_sum = sum(even)
    odd_sum = sum(odd)
    
    print(f'Even numbers: {even}', f'| Even numbers sum: {even_sum}')
    print(f'Odd numbers: {odd}', f'| Even numbers sum: {odd_sum}')