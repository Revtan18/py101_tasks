"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def even_numbers():
    numbers_list = list(map(int, input().split()))
    even = [number for number in numbers_list if number % 2 == 0]
    if even != []:
        print(f"You wrote {len(even)} even numbers")
    else:
        print("You did not write even numbers")


even_numbers()
    


# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."

def sell_alcohol():
    print("Вот ваша алкашка. Но знайте, однажды вы пожалеете об этом")

age = 17
x = print("Мы не продаём алкоголь несовершеннолетним.") if age < 21 else sell_alcohol()


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()

import keyword
def keyword_check(word):
    if keyword.iskeyword(word) == True:
        print("This string is a keyword")
    else:
        print("You are normal programmer")

keyword_check('and')
keyword_check('lol')

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."

def get_type(obj):
    types_dictionaries = {'int': 'число', 'str': 'строка', 'bool': 'булевый', 'Nonetype': 'None', 'list': 'список', 'tuple': 'кортеж', 'set': 'множество', 'dict': 'словарь'}
    print("Это " + types_dictionaries[type(obj).__name__])

get_type(32)
