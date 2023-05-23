a = int(input('А: '))
b = int(input('B: '))

print('Четные числа на отрезке:')  

for i in range(a, b+1):
    if i % 2 == 0:
        print(i)