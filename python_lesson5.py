# Создайте список слов: ['banana', 'apple', 'cherry', 'date', 'elderberry']
# 1. Отсортируйте слова по алфавиту
# 2. Разверните список в обратном порядке
# 3. Используя цикл, выведите каждое слово в верхнем регистре
# 4. Подсчитайте количество слов, которые начинаются на гласную


# list = ['banana', 'apple', 'cherry', 'date', 'elderberry']
# list.sort()
# print(list)
# list.reverse()
# print(list)

# for i in list:
#     print(i.upper())

# letters="eyioa"
# sum=0
# for i in list:
#     if i[0] in letters:
#         sum=sum+1
#         print(sum)
#     else:
#         pass
    


# Создайте список текстов с пробелами: [' hello ', '  world  ', ' python ']
# 1. Используя цикл, удалите пробелы в начале и конце каждого слова
# 2. Замените все оставшиеся пробелы на подчеркивания
# 3. Переведите все в нижний регистр
# 4. Создайте новый список с очищенными данными


# list = [' hello ', '  world  ', ' python ']
# # list1 = []
# # for i in list:

# #     list1.append(i.strip(' '))

# # print(list1)

# list2 = []
# # for i in list:
# #     list2.append(i.replace(' ', '_'))

# # print(list2)

# list.clear()
# print(list)



# Создайте список: [1, 5, 2, 8, 5, 3, 5, 9, 5, 2]
# 1. Найдите индекс первого числа 5
# 2. Подсчитайте, сколько раз встречается 5
# 3. Используя цикл и индексы, выведите все позиции где стоит 5
# 4. Удалите первое вхождение 5
# 5. Выведите обновленный список

# list = [1, 5, 2, 8, 5, 3, 5, 9, 5, 2]
# for i in list :
#     if i == 5:
#         print(list.index(i))
#         break
#     else:
#         pass


# sum=0
# for i in list:
#     if i == 5:
#         sum=sum+1
#         print(sum)
#     else:
#         pass


# list = [1, 5, 2, 8, 5, 3, 5, 9, 5, 2]
# for i in range(len(list)):
#     if list[i] == 5:
#         print (i,list[i])
#     else: 
#         pass


# for i in list :
#     if i == 5:
#         list.remove(i)
#         break
#     else:
#         pass
# print(list)



# Создайте список студентов: ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# Используя range(len(...)):
# 1. Выведите всех студентов с их номерами (1, 2, 3, и т.д.)
# 2. Выведите номер студента 'Виктор'
# 3. Вставьте нового студента 'Евгений' на позицию 2
# 4. Выведите обновленный список с номерами


# list = ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']

# for i in range(len(list)):
#     print(i,list[i])

# for i in list:
#     if i == 'Виктор':
#         print(list.index(i))
#     else:
#         pass

# list.insert(2,'Евгений')

# print(list)



# Создайте список чисел: [2, 4, 6, 8, 10, 12, 15, 18, 20]
# 1. Создайте новый список, где каждое число умножено на 5
# 2. Создайте новый список, где каждое число возведено в квадрат
# 3. Создайте новый список только из чисел, которые делятся на 3
# 4. Объедините первые два списка в один
# Выведите все три новых списка


# nums = [2, 4, 6, 8, 10, 12, 15, 18, 20]
# nums1 =[]
# nums2 = []
# for i in nums:
#     nums1.append(i*5)
# print(nums1)

# for i in nums:
#     nums2.append(i**2)
# print(nums2)

# # for i in nums:
# #     if i%3==0:
# #         nums1.append(i)
# # print(nums1)

# nums1.extend(nums2)
# print(nums1)



# Создайте список слов: ['python', 'javascript', 'go', 'rust', 'java', 'cpp']
# 1. Найдите самое длинное слово
# 2. Найдите самое короткое слово
# 3. Используя цикл, выведите каждое слово с его:
#    - Первой буквой
#    - Последней буквой
#    - Длиной
# 4. Создайте новый список слов в верхнем регистре
# 5. Подсчитайте количество слов, которые содержат букву 'p'


# list = ['python', 'javascript', 'go', 'rust', 'java', 'cpp']

# max = 0
# min=len(list[0])
# new_list =[]

# for i in list:
#     if len(i)>max:
#         max=len(i)
# print(max)

# for i in list:
#     if len(i) == max:
#         print(i)

# for i in list:

#     if len(i)<min:
#         min=len(i)
# print(min)

# for i in list:
#     if len(i) == min:
#         print(i)

# for i in list:
#     print(i + " " +i[0])

# for i in list:
#     print(i + " " +i[-1])

# for i in list:
#     print(i, len(i))

# for i in list:
#     new_list.append(i.upper())

# print(new_list)

# for i in list:
#     if i.startswith('p'):
#         max=max+1
#     else:
#         pass
# print(max)



# Создайте таблицу умножения для чисел от 2 до 5
# 1. Для каждого числа от 2 до 5 создайте его таблицу умножения (от 1 до 10)
# 2. Выведите таблицу в формате: "Таблица 2: 2 * 1 = 2, 2 * 2 = 4, ..."
# 3. Создайте список всех произведений
# 4. Подсчитайте количество произведений > 20 и < 30
# 5. Найдите максимальное произведение

# list2 = []
# list3 = []
# list4 = []
# list5 = []
# list = []

# max = 0
# min = 0
# num=0

# print("Таблица 2: ")

# for i in range(1, 11):
#     print(f"{i} * 2 = {i * 2}")
#     list2.append(i*2)

# print(list2)

# print("Таблица 3: ")

# for i in range(1, 11):
#     print(f"{i} * 3 = {i * 3}")
#     list3.append(i*3)

# print(list3)

# print("Таблица 4: ")

# for i in range(1, 11):
#     print(f"{i} * 4 = {i * 4}")
#     list4.append(i*4)

# print(list4)

# print("Таблица 5: ")

# for i in range(1, 11):
#     print(f"{i} * 5 = {i * 5}")
#     list5.append(i*5)

# print(list5)

# list.extend(list2)
# list.extend(list3)
# list.extend(list4)
# list.extend(list5)

# print(list)

# for i in list:
#     if i > 20:
#         max=max+1
#     elif i < 30:
#         min = min +1
#     else:
#         pass
        

# print("Количество произведени больше 20:" , max)
# print("Количество произведени меньше 30:" , min)

# for i in list:
#     if i>num:
#         num=i
# print(num)



# Создайте список: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 1. Отсортируйте список
# 2. Разверните в обратном порядке
# 3. Подсчитайте все элементы
# 4. Подсчитайте сколько раз встречается число 5
# 5. Найдите индекс первого числа 1
# 6. Удалите первое число 1
# 7. Выведите список после каждой операции

# list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# list.sort()
# list.reverse()
# print(len(list))
# num = 0

# for i in list:
#     if i==5:
#         num = num+1

# print(num)

# for i in list:
#     if i==1:
#         print(i, list.index(i))
#         break


# for i in list:
#     if i==1:
#         list.pop(i)
#         break

# print(list)


# Создайте список фраз:
# ['Привет мир', 'Python очень крутой', 'Я люблю программирование', 'Это отлично', 'JavaScript сложный']
# 1. Найдите все фразы, которые содержат букву 'о'
# 2. Создайте новый список фраз длиной > 20 символов
# 3. Замените все пробелы на подчеркивания в каждой фразе
# 4. Создайте новый список с первым словом каждой фразы
# 5. Подсчитайте общее количество слов во всех фразах


# list = ['Привет мир', 'Python очень крутой', 'Я люблю программирование', 'Это отлично', 'JavaScript сложный']
# list2 = []
# sum=0

# for i in list:
#     if 'о' in i:
#         print(i)

# for i in list:
#     if len(i)>20:
#         print(i)
#         list2.append(i)
# print(list2)

# for i in list:
#     print(i.replace(' ', '_'))

# for i in list:
#     a=i.split()[0]
#     list2.append(a)
# print(list2)

# for i in list:
#     a= len(i.split())
#     sum=sum+a

# print(sum)



# Создайте списки:
# numbers = [1, 2, 3, 4]
# letters = ['a', 'b', 'c']
#
# 1. Создайте новый список, где каждое число соединено с каждой буквой
#    Результат: ['1a', '1b', '1c', '2a', '2b', '2c', ...]
#
# 2. Создайте новый список со строками "число-буква" для пар:
#    ['1-a', '2-b', '3-c', '4-?']
#    (если букв меньше, пропустите оставшиеся числа)
#
# 3. Для каждой пары выведите информацию
#
# 4. Используйте extend() для объединения списков



numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c']
list=[]

for i in numbers:
    for j in letters:
        list.append(str(i)+j)
        
        

print(list)
        
