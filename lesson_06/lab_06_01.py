n = int(input('Введите количество элементов: '))

count = 0

for i in range(0, n):
    k = int(input('Введите целое число: '))
    if k == 0:
        count += 1

print('Количество нулевых элементов: ', count)    