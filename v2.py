import collections

# Изначальный словарь питомцев
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

# Функция для получения информации о питомце по его ID
def get_pet(ID):
    return pets[ID] if ID in pets else False

# Функция для правильного выбора суффикса возраста
def get_suffix(age):
    if 11 <= age % 100 <= 19:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

# Функция для отображения списка всех питомцев
def pets_list():
    if not pets:
        print("Список питомцев пуст.")
        return
    for ID, pet_data in pets.items():
        for name, details in pet_data.items():
            age = details["Возраст питомца"]
            print(f'{ID}. Это {details["Вид питомца"]} по кличке "{name}". Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {details["Имя владельца"]}')

# Функция для создания новой записи о питомце
def create():
    last = collections.deque(pets, maxlen=1)[0]  # Получаем последний ID
    new_id = last + 1  # Увеличиваем идентификатор на 1
    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец {name} добавлен с ID {new_id}.")

# Функция для чтения информации о питомце
def read():
    pet_id = int(input("Введите ID питомца: "))
    pet = get_pet(pet_id)
    if pet:
        for name, details in pet.items():
            age = details["Возраст питомца"]
            print(f'Это {details["Вид питомца"]} по кличке "{name}". Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {details["Имя владельца"]}.')
    else:
        print("Питомец с таким ID не найден.")

# Функция для обновления информации о питомце
def update():
    pet_id = int(input("Введите ID питомца для обновления: "))
    pet = get_pet(pet_id)
    if pet:
        for name in pet:
            new_name = input(f"Введите новую кличку питомца (текущая: {name}): ") or name
            new_type = input(f"Введите новый вид питомца (текущий: {pet[name]['Вид питомца']}): ") or pet[name]["Вид питомца"]
            new_age = input(f"Введите новый возраст питомца (текущий: {pet[name]['Возраст питомца']}): ")
            new_age = int(new_age) if new_age else pet[name]["Возраст питомца"]
            new_owner = input(f"Введите новое имя владельца (текущее: {pet[name]['Имя владельца']}): ") or pet[name]["Имя владельца"]
            pets[pet_id] = {
                new_name: {
                    "Вид питомца": new_type,
                    "Возраст питомца": new_age,
                    "Имя владельца": new_owner
                }
            }
            print(f"Информация о питомце с ID {pet_id} обновлена.")
    else:
        print("Питомец с таким ID не найден.")

# Функция для удаления питомца
def delete():
    pet_id = int(input("Введите ID питомца для удаления: "))
    if pet_id in pets:
        del pets[pet_id]
        print(f"Питомец с ID {pet_id} удален.")
    else:
        print("Питомец с таким ID не найден.")

# Основной цикл программы
command = ""
while command != "stop":
    command = input("Введите команду (create, read, update, delete, list, stop): ")
    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Программа завершена.")
    else:
        print("Неизвестная команда. Попробуйте снова.")
