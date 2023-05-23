word = input('Введите слово из маленьких латинских букв: ')

a, e, i, o, u = 0, 0, 0, 0, 0 
vowels = 0
cons = 0
consonants = 'qzwsxdcrfvtgbyhnjmklp'

for letter in word:
    if letter in consonants:
        cons += 1
    elif letter == 'a':
        vowels += 1
        a += 1
    elif letter == 'e':
        vowels += 1
        e += 1
    elif letter == 'i':
        vowels += 1
        i += 1
    elif letter == 'o':
        vowels += 1
        o += 1
    elif letter == 'u':
        vowels += 1
        u += 1

print('Общее количество согласных: ', cons)
print('Общее количество гласных: ', vowels)
print('Гласные:')
print(f'a - {a}' if a else 'a - False')
print(f'e - {e}' if e else 'e - False')
print(f'i - {i}' if i else 'i - False')
print(f'o - {o}' if o else 'o - False')
print(f'u - {u}' if u else 'u - False')
    
