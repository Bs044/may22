#Это более сложное и извращенное решение третьей задачи, точнее усовершенствованное решение третьей задачи
#для проверки и работы программы покамись пользователь не начнет следовать всем условиям программы


while True:
    number_input = input('Введите шестизначное число: ')
    if len(number_input) < 6 or len(number_input) > 6:
        print('Вы ввели не шестезначное число, попробуйте еще раз!')
        continue
    elif len(number_input) == 6:
        half_one = len(number_input)
        half_two = half_one // 2

        one = number_input[half_two:half_one]
        two = number_input[0:half_two]
        try: 
            one = int(one)
            two = int(two)
            result = one + two
        except ValueError:
            print('Видимо вы ввели не число, попробуйте еще раз :/')
            continue
        print(result)
        break
