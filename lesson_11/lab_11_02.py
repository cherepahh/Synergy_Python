import collections

pets = {
    1: {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        }
}

def get_pet(ID):
  return pets[ID] if ID in pets.keys() else False


def get_suffix(value):
    year = 'лет'
    if value <= 4 or value >= 21:
        flag = value % 10
        if flag == 1: 
            year = 'год'
        elif flag < 5: 
            year = 'года'
    return year


def create(name, view, age, owner):
    last = collections.deque(pets, maxlen=1)[0]
    pets[last + 1] = {
        name: {
            "Вид питомца": view,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }


def read(ID):
    pet = get_pet(ID)
    if pet:
        name = list(pet.keys())[0]
        pet = pet[name]
        print (f'Это {pet["Вид питомца"]} по кличке "{name}". Возраст питомца: {pet["Возраст питомца"]} {get_suffix(pet["Возраст питомца"])}. Имя владельца: {pet["Имя владельца"]}' )
    else: 
        print("Питомец не найден")


def update(ID, name, view, age, owner):
    pet = get_pet(ID)
    if pet:
        pets[ID] = {
            name: {
                "Вид питомца": view,
                "Возраст питомца": age,
                "Имя владельца": owner
            }
        }
    else: 
         print("Питомец не найден")


def delete(ID):
    pet = get_pet(ID)
    if pet: 
       pets.pop(ID)
    else: 
       print("Питомец не найден")


def pets_list():
   for i in pets.keys():
        read(i)

command = ''

while command != 'stop':
    command = input(\
         'Выберите действие: \n\
          create - добавить запись, \n\
          read - вывести запись, \n\
          update - обновить запись, \n\
          delete - удалить запись, \n\
          list - вывести все записи, \n\
          stop - завершить программу. \n\
          Ваш выбор: ')

    if command == 'create':
        name = input('Введите имя питомца: ')
        view = input('Введите вид питомца: ')
        age = int(input('Введите возраст питомца: '))
        owner = input('Введите имя владельца: ')
        create(name, view, age, owner)
    elif command == 'read':
        ID = int(input('Введите id питомца: '))
        read(ID)
    elif command == 'update':
        ID = int(input('Введите id питомца: '))
        name = input('Введите новое имя питомца: ')
        view = input('Введите новый вид питомца: ')
        age = int(input('Введите новый возраст питомца: '))
        owner = input('Введите новое имя владельца: ')
        update(ID, name, view, age, owner)
    elif command == 'delete':
      ID = int(input('Введите id питомца: '))
      delete(ID)
    elif command == 'list':
        pets_list()