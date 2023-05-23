def min_boats(m, weights):
    weights.sort()
    num_boats = 0
    i, j = 0, len(weights) - 1
    while i <= j:
        if weights[i] + weights[j] <= m:
            i += 1
        j -= 1
        num_boats += 1
    return num_boats

m = int(input('Введите вместимость лодки: '))
n = int(input('Введите количество рыбаков: '))

weights = []
for i in range(n):
    weights.append(int(input(f'Введите вес {i+1} рыбака: ')))

print('Минимальное количество лодок: ', min_boats(m, weights))