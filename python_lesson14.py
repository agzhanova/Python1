# 1. Создайте декоратор add_prefix(func)
# 2. Декоратор должен добавить "★ " перед результатом функции
# 3. Примените декоратор к функции greeting(name)
# 4. Функция greeting возвращает "Привет, {name}!"
#
# Пример:
# @add_prefix
# def greeting(name):
#     return f"Привет, {name}!"
#
# greeting('Алиса') → "★ Привет, Алиса!"
# greeting('Боб') → "★ Привет, Боб!"

# def add_prefix(func):
#     def wrapper(a):
#         b=func(a)
#         return f'★ {b}'
#     return wrapper
    

# @add_prefix
# def greeting(name):
#     return f'Привет, {name}!'

# print(greeting('Zhaina'))


# 1. Создайте декоратор check_positive(func)
# 2. Декоратор должен проверить что число > 0
# 3. Если число положительное — вызвать функцию
# 4. Если число отрицательное — вернуть "Ошибка: число должно быть положительным"
# 5. Примените к функции square(x)
#
# Пример:
# @check_positive
# def square(x):
#     return x ** 2
#
# square(5) → 25
# square(-3) → "Ошибка: число должно быть положительным"

# def check_positive(func):
#     def wrapper(x):
#         if x>0:
#             result=func(x)
#             return result
#         else:
#             return 'Ошибка: число должно быть положительным'
#     return wrapper



# @check_positive
# def square(x):
#     return x ** 2

# print(square(2))
# print(square(-2))


# 1. Создайте декоратор uppercase(func)
# 2. Декоратор должен преобразовать результат в ВЕРХНИЙ РЕГИСТР
# 3. Используйте .upper()
# 4. Примените к функции message(text)
#
# Пример:
# @uppercase
# def message(text):
#     return text
#
# message('привет мир') → "ПРИВЕТ МИР"
# message('hello') → "HELLO"


# def uppercase(func):
#     def wrapper(text):
#         result=func(text)
#         return result.upper()
#     return wrapper

# @uppercase
# def message(text):
#     return text

# print(message('zhaina'))


# 1. Создайте декоратор count_calls(func)
# 2. Декоратор должен подсчитать количество вызовов функции
# 3. Перед каждым вызовом выводить "Вызов номер X"
# 4. Примените к функции multiply(a, b)
#
# Пример:
# @count_calls
# def multiply(a, b):
#     return a * b
#
# multiply(3, 4)  → Вызов номер 1 / 12
# multiply(5, 6)  → Вызов номер 2 / 30
# multiply(2, 7)  → Вызов номер 3 / 14


# def count_calls(func):
#     count=[0]
#     def wrapper(a,b):
#         count[0]+=1
#         result=func(a,b)
#         return f'Вызов номер {count[0]} \n{result}' 
#     return wrapper


# @count_calls
# def multiply(a, b):
#     return a * b


# print(multiply(1,2))
# print(multiply(3,5))



# 1. Создайте декоратор add_brackets(func)
# 2. Декоратор должен обвести результат в скобки: [результат]
# 3. Примените к функции concat(a, b)
#
# Пример:
# @add_brackets
# def concat(a, b):
#     return a + b
#
# concat('hello', ' world') → "[hello world]"
# concat('Python', ' is cool') → "[Python is cool]"
# concat('1', '2') → "[12]"


# def add_brackets(func):
#     def wrapper(a,b):
#         result=func(a,b)
#         return f'[{result}]'
#     return wrapper


# @add_brackets
# def concat(a, b):
#     return a + b

# print(concat('hello', ' world'))
# print(concat('Python', ' is cool'))
# print(concat('1', '2'))