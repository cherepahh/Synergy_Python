a = set()
b = set()

n = int(input('Введите длину 1 списка: '))
for i in range(n):
    a.add(int(input('Введите число: ')))

n = int(input('Введите длину 2 списка: '))
for i in range(n):
    b.add(int(input('Введите число: ')))

print('Количество чисел, содержащихся в обоих списках: ', len(a.intersection(b)))