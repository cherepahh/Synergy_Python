n = int(input('Введите количество чисел: '))
a = set(map(int, input('Введите числа через пробел: ').split()))
print('Количество различных чисел:', len(a))