# 1. Напишите функцию multiply(a, b)
# 2. Функция должна возвращать произведение двух чисел
# 3. Вызовите функцию с разными числами


# def multiply(a, b):
#     """Функция возвращает произведение двух чисел"""
#     print (a*b)
# multiply(3, 4)
# multiply(5, 6)
# multiply(2, 9)


# 1. Напишите функцию greet(name, greeting='Привет')
# 2. Функция должна возвращать строку "{greeting}, {name}!"
# 3. Вызовите функцию двумя способами:
#    - С одним аргументом (используется значение по умолчанию)
#    - С двумя аргументами (переданное значение)
#
# Пример:
# greet('Алиса') → "Привет, Алиса!"
# greet('Боб', 'Привет') → "Привет, Боб!"
# greet('Виктор', 'Добрый день') → "Добрый день, Виктор!"

# def greet(name, greeting='Привет'):
#     """Функция возвращает строку "{greeting}, {name}!"""
#     print(f'{greeting}, {name}')
# greet('Алиса')
# greet('Боб', 'Привет')
# greet('Виктор', 'Добрый день')

# 1. Напишите функцию info(name, age=18, city='Алматы')
# 2. Функция должна возвращать строку с информацией о человеке
# 3. Вызовите функцию разными способами
#
# Пример:
# info('Алиса') → "Алиса, 18 лет, Алматы"
# info('Боб', 25) → "Боб, 25 лет, Алматы"
# info('Виктор', 30, 'Астана') → "Виктор, 30 лет, Астана"


# def info(name, age=18, city='Алматы'):
#     """Функция возвращает строку с информацией о человеке"""
#     print(f'{name}, {age}, {city}')

# info('Алиса')
# info('Боб', 25)
# info('Виктор', 30, 'Астана')


# 1. Напишите функцию sum_numbers(*args)
# 2. Функция должна возвращать сумму всех переданных чисел
# 3. Используйте функцию sum() для подсчета
# 4. Вызовите функцию с разным количеством аргументов
#
# Пример:
# sum_numbers(1, 2, 3) → 6
# sum_numbers(5, 10, 15, 20) → 50
# sum_numbers(1) → 1
# sum_numbers(100, 200, 300, 400, 500) → 1500

# def sum_numbers(*args):
#     """Функция возвращает сумму всех переданных чисел"""
#     print(sum(args))

# sum_numbers(1, 2, 3)
# sum_numbers(5, 10, 15, 20)
# sum_numbers(1)
# sum_numbers(100, 200, 300, 400, 500)


# 1. Напишите функцию print_items(*args)
# 2. Функция должна вывести каждый элемент на новой строке с номером
# 3. Используйте цикл for и enumerate()
# 4. Вызовите функцию с разными элементами

# def print_items(*args):
#     """Функция  покажет каждый элемент на новой строке с номером"""
#     for i,j in enumerate(args):
#         print(f'{i+1}. {j}')
# print_items('apple', 'banana', 'cherry')


# 1. Напишите функцию count_strings(*args)
# 2. Подсчитайте сколько строк (str) в аргументах
# 3. Используйте isinstance(элемент, str) для проверки
# 4. Возвращайте количество строк
#

# def count_strings(*args):
#     count=0
#     for i in args:
#         if isinstance(i,str):
#             count+=1
#     print(count)
# count_strings('hello', 5, 'world', 10, 'test')
# count_strings(1, 2, 3, 4, 5)
# count_strings('a', 'b', 'c')

# 1. Напишите функцию create_person(**kwargs)
# 2. Функция должна вывести информацию о человеке из словаря
# 3. Используйте цикл for и .items() для вывода
# 4. Вызовите функцию с разными параметрами

# def create_person(**kwargs):
#     """Функция покажет информацию о человеке из словаря"""
#     for i, j in kwargs.items():
#         print(f'{i}: {j}')
# create_person(name='Алиса', age=20, city='Алматы')

# 1. Напишите функцию introduce(name, age, *hobbies)
# 2. name и age — обязательные параметры
# 3. hobbies — остальные аргументы (хобби)
# 4. Выведите: имя, возраст и все хобби


# def introduce(name, age, *hobbies):
#     a=','.join(map(str,hobbies))
#     print(f'Имя: {name} \nВозраст: {age} \nХобби: {a}')
# introduce('Алиса', 20, 'Читать', 'Рисовать', 'Программировать')

# 1. Напишите функцию show_data(name, *numbers, **info)
# 2. name — обязательный параметр
# 3. numbers — все остальные числовые аргументы
# 4. info — все остальные именованные аргументы (словарь)
# 5. Выведите все данные структурированно
#
# Пример:
# show_data('Али', 10, 20, 30, city='Алматы', job='Engineer')
# Вывод:
# Имя: Али
# Числа: (10, 20, 30)
# Информация:
# city: Алматы
# job: Engineer


# def show_data(name, *numbers, **info):
#     a=','.join(map(str,numbers))
#     print(f'Имя: {name} \nЧисла: {a} \nИнформация:')
#     for i,j in info.items():
#         print(f'{i}: {j}')

# show_data('Али', 10, 20, 30, city='Алматы', job='Engineer')


# 1. Напишите функцию apply_operation(operation, *numbers)
# 2. operation — функция, которую применять
# 3. numbers — числа, к которым применять функцию
# 4. Используйте map() для применения функции
# 5. Возвращайте список результатов
#
# Пример:
# def double(x):
#     return x * 2
#
# apply_operation(double, 1, 2, 3, 4, 5)
# → [2, 4, 6, 8, 10]
#
# def square(x):
#     return x ** 2
#
# apply_operation(square, 1, 2, 3, 4, 5)
# → [1, 4, 9, 16, 25]

def apply_operation(operation, *numbers):
    print(list(map(operation,numbers)))
apply_operation(lambda x: x*2, 1, 2, 3, 4, 5)
apply_operation(lambda x: x**2, 1, 2, 3, 4, 5)
