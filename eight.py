cena = input('Введите стоимость товара в "$": ')
skidka = input('Введите процент скидки: ')
cena = int(cena)
skidka = int(skidka)
sum_skidka = cena / 100 * skidka
result = cena - sum_skidka

print(f'Цена товара: {cena}\nСкидка в процентах: {skidka}%\nИтого вы должны заплатить: {result}$')

