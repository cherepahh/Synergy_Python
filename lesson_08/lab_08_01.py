n = int(input('Введите размер списка: '))

a = []
for i in range(n):
    a.append(int(input('Введите число: ')))

print('Перевернутый массив: ', a[::-1])