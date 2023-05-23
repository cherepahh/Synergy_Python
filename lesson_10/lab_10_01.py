pets = {}

name = input('Введите имя питомца: ')
view = input('Введите вид питомца: ')
age = int(input('Введите возраст питомца: '))
owner = input('Введите имя владельца: ')

pets[name] = {
    "Вид питомца": view,
    "Возраст питомца": age,
    "Имя владельца": owner
  }

res = ''

for key, value in pets[name].items():
    if key == 'Вид питомца':
        res = f'Это {value} по кличке "{name}". '
    elif key == 'Возраст питомца':
        year = 'лет'
        if value <= 4 or value >= 21:
            flag = value % 10
            if flag == 1: 
                year = 'год'
            elif flag < 5: 
                year = 'года'
        res = res + 'Возраст: ' + str(value) + ' ' + year
    if key == 'Имя владельца':
        res = res + '. Имя владельца: ' + value

print(res)