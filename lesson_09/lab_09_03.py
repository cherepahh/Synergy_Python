a = list(map(int, input('Введите числа последовательности через пробел: ').split()))
b = set()

for i in a:
    if i in b:
        print(f'{i} - YES')
    else:
        print(f'{i} - NO')
        b.add(i)