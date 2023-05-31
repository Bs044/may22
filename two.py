word = input('введите слово: ')
a = len(word)
b = a // 2
c = word[b:a]
d = word[0:b]

print(d, c)