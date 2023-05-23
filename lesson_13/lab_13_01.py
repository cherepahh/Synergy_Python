import random

def generate(n, m):
    a = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = random.randint(-100, 100)
    return a

def summ(a, b, n, m):
    res = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            res[i][j] = a[i][j] + b[i][j]
    return res

def output(a):
    for i in a:
        print(i)

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

matrix_1 = generate(n, m)
matrix_2 = generate(n, m)

print('Матрица №1:')
output(matrix_1)
print('Матрица №2:')
output(matrix_2)

matrix_3 = summ(matrix_1, matrix_2, n, m)
print('Сумма матриц:')
output(matrix_3)