
day= input('Введите день вашего рождения: ')
month = input('Введите месяц вашего рождения: ')
year = input('Введите год вашего рождения: ')

day, month  = int(day), int(month)

if day == 1 or day == 2 or day == 3 or day  == 4 or day == 5 or day == 6 or day == 7 or day == 8 or day == 9:
    day = f'0{day}'
if month == 1 or month == 2 or month == 3 or month == 4 or month== 5 or month == 6 or month == 7 or month == 8 or month == 9:
    month = f'0{month}'

print(f'Ваша дата рождения в формате "дд.мм.гггг": {day}.{month}.{year}')