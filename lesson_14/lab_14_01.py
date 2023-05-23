def recursive(a):
    if len(a) == 0:
        print('Конец списка')
    else:
        print(a[0])
        recursive(a[1::])

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
recursive(my_list)