word  = input('Введите слово: ')
middle = len(word[1:-1])
first = word[0]
last = word[-1]
result_middle = '*' * middle
print(f'{first}{result_middle}{last}')