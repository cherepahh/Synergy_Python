def fact(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

n = int(input('Введите натуральное число: '))
f = fact(n)
print(f'Факториал числа {n}: {f}')

print('Список факториалов:')
lst = []
for i in range(f, 0, -1):
    lst.append(fact(i))
print(lst)