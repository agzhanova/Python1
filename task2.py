# Создайте список слов: ['banana', 'apple', 'cherry', 'date', 'elderberry']
# 1. Отсортируйте слова по алфавиту
# 2. Разверните список в обратном порядке
# 3. Используя цикл, выведите каждое слово в верхнем регистре
# 4. Подсчитайте количество слов, которые начинаются на гласную


# words= ['banana', 'apple', 'cherry', 'date', 'elderberry']
# words.sort()
# words.reverse()
# text='eyuioa'
# c=0
# for i in words:
#     a=i.upper()
#     print(a)
# for i in words:
#     if i[0] in text:
#         c+=1
# print(c)

# Создайте список текстов с пробелами: [' hello ', '  world  ', ' python ']
# 1. Используя цикл, удалите пробелы в начале и конце каждого слова
# 2. Замените все оставшиеся пробелы на подчеркивания
# 3. Переведите все в нижний регистр
# 4. Создайте новый список с очищенными данными

# lst=[' hello ', '  world  ', ' python ']
# lst1=[]
# for i in lst:
#     a=i.strip().replace(' ','_')
#     b=a.lower()
#     lst1.append(b)
# print(lst1)

# Создайте список: [1, 5, 2, 8, 5, 3, 5, 9, 5, 2]
# 1. Найдите индекс первого числа 5
# 2. Подсчитайте, сколько раз встречается 5
# 3. Используя цикл и индексы, выведите все позиции где стоит 5
# 4. Удалите первое вхождение 5
# 5. Выведите обновленный список

# nums=[1, 5, 2, 8, 5, 3, 5, 9, 5, 2]
# for i in nums:
#     if i==5:
#         print(nums.index(i))
#         break
# c=0
# for i in nums:
#     if i==5:
#         c+=1
# print(c)
# for i in range(len(nums)):
#     if nums[i]==5:
#         print(i)

# for i in nums:
#     if i==5:
#         nums.remove(i)
#         break
# print(nums)

# Создайте список студентов: ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# Используя range(len(...)):
# 1. Выведите всех студентов с их номерами (1, 2, 3, и т.д.)
# 2. Выведите номер студента 'Виктор'
# 3. Вставьте нового студента 'Евгений' на позицию 2
# 4. Выведите обновленный список с номерами

# students=['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# for i in range(len(students)):
#     num=i+1
#     print(f'{num}. {students[i]}')

# a= students.index('Виктор')+1
# print(a)
# students.insert(2,'Евгений')
# for i in range(len(students)):
#     num=i+1
#     print(f'{num}. {students[i]}')


# Создайте список чисел: [2, 4, 6, 8, 10, 12, 15, 18, 20]
# 1. Создайте новый список, где каждое число умножено на 5
# 2. Создайте новый список, где каждое число возведено в квадрат
# 3. Создайте новый список только из чисел, которые делятся на 3
# 4. Объедините первые два списка в один
# Выведите все три новых списка

# nums=[2, 4, 6, 8, 10, 12, 15, 18, 20]
# nums2=[]
# num3=[]
# num4=[]
# for i in nums:
#     nums2.append(i*2)
# for i in nums:
#     num3.append(i**2)
# for i in nums:
#     if i%3==0:
#         num4.append(i)
# nums2.extend(num3)
# print(nums2)
# print(num3)
# print(num4)


# Создайте список слов: ['python', 'javascript', 'go', 'rust', 'java', 'cpp']
# 1. Найдите самое длинное слово
# 2. Найдите самое короткое слово
# 3. Используя цикл, выведите каждое слово с его:
#    - Первой буквой
#    - Последней буквой
#    - Длиной
# 4. Создайте новый список слов в верхнем регистре
# 5. Подсчитайте количество слов, которые содержат букву 'p'


# words=['python', 'javascript', 'go', 'rust', 'java', 'cpp']
# mx=0
# mn=len(words[0])
# a=''
# for i in words:
#     if len(i)>mx:
#         mx=len(i)
#         a=i
# print(a)

# for i in words:
#     if len(i)<mn:
#         mn=len(i)
#         a=i
# print(a)

# for i in words:
#     print(f'{i} первая буква {i[0]}')
#     print(f'{i} последняя буква {i[-1]}')
#     b=len(i)
#     print(f'{i} длина {b}')

# lst=[]

# for i in words:
#     lst.append(i.upper())
# print(lst)

# w=0
# for i in words:
#     if 'p' in i:
#         w+=1
# print(w)


# Создайте таблицу умножения для чисел от 2 до 5
# 1. Для каждого числа от 2 до 5 создайте его таблицу умножения (от 1 до 10)
# 2. Выведите таблицу в формате: "Таблица 2: 2 * 1 = 2, 2 * 2 = 4, ..."
# 3. Создайте список всех произведений
# 4. Подсчитайте количество произведений > 20 и < 30
# 5. Найдите максимальное произведение

# list2=[]
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

# nums=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# nums.sort()
# nums.reverse()
# print(nums)
# print(len(nums))
# c=0
# for i in nums:
#     if i==5:
#         c+=1
# print(c)
# for i in nums:
#     if i==1:
#         print(nums.index(i))
#         break
# for i in nums:
#     if i==1:
#         nums.remove(i)
#         break
# print(nums)


# Создайте список фраз:
# ['Привет мир', 'Python очень крутой', 'Я люблю программирование', 'Это отлично', 'JavaScript сложный']
# 1. Найдите все фразы, которые содержат букву 'о'
# 2. Создайте новый список фраз длиной > 20 символов
# 3. Замените все пробелы на подчеркивания в каждой фразе
# 4. Создайте новый список с первым словом каждой фразы
# 5. Подсчитайте общее количество слов во всех фразах

# lst=['Привет мир', 'Python очень крутой', 'Я люблю программирование', 'Это отлично', 'JavaScript сложный']
# lst2=[]
# for i in lst:
#     if 'о' in i:
#         print(i)
# for i in lst:
#     if len(i)>20:
#         lst2.append(i)
# print(lst2)
# for i in lst:
#     a=i.replace(' ','_')
#     print(a)
# lst3=[]
# for i in lst:
#     lst3.append(i.split(' ')[0])
    
# print(lst3)

# for i in lst:
#     n=len(i.split(' '))
#     print(n)


