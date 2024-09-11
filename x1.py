# Шаг 1: Создайте пустой словарь
pets = {}

# Шаг 2: Соберите данные о питомце с помощью функции input()
name = input("Введите имя питомца: ")
species = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

# Шаг 3: Добавьте собранные данные в словарь pets
pets[name] = {
    'Вид питомца': species,
    'Возраст питомца': age,
    'Имя владельца': owner
}

# Шаг 4: Определите правильное склонение для возраста питомца
def age_suffix(age):
    if 10 <= age % 100 <= 20:
        return 'лет'
    if age % 10 == 1:
        return 'год'
    if age % 10 in [2, 3, 4]:
        return 'года'
    return 'лет'

age_text = age_suffix(age)
print(f"Возраст питомца: {age} {age_text}")

# Шаг 5: Выведите информацию о питомце
pet_info = pets[name]
pet_description = (
    f"Это {pet_info['Вид питомца']} по кличке '{name}'. "
    f"Возраст питомца: {age} {age_text}. Имя владельца: {pet_info['Имя владельца']}."
)
print(pet_description)
