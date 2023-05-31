number_input = input('Введите шестизначное число: ')

half_one = len(number_input)
half_two = half_one // 2

one = number_input[half_two:half_one]
two = number_input[0:half_two]

one = int(one)
two = int(two)
result = one + two

print(result)
