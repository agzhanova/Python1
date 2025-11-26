# n1=input('Укажите ход:')
# n2=input('Укажите ход:')

# def rps(p1, p2):
#     if p1==p2:
#         return 'Draw!'
#     elif p1== 'scissors' and p2=='paper':
#         return 'Player 1 won!'
#     elif p1=='rock' and p2=='scissors':
#         return 'Player 1 won!'
#     elif p1=='paper' and p2=='rock':
#         return 'Player 1 won!'
#     else :
#         return 'Player 2 won!'
# print(rps(n1,n2))


# def is_palindrome(s):
#     if s==s[::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome('Kasue'))

# def sum_array(a):
#      if a==list():
#          return 0
#      else:
#          return sum(a)
# print(sum_array([]))
# print(sum_array([1,2,3]))


# def quarter_of(month):
#     if month==1 or month==2 or month==3:
#         return 1
#     elif month==4 or month==5 or month==6:
#         return 2
#     elif month==7 or month==8 or month==9:
#         return 3
#     elif month==10 or month==11 or month==12:
#         return 4
# cat=24
# dog=24
# def human_years_cat_years_dog_years(human_years):
#     if human_years==1:
#         return human_years,cat-9,dog-9
#     elif human_years==2:
#         return human_years,cat,dog
#     else:
#         return human_years,cat+8*4,dog+8*5
    
# print(human_years_cat_years_dog_years(25))


# def better_than_average(class_points, your_points):
#     if sum(class_points)/len(class_points)<your_points:
#         return True
#     else:
#         return False
    


# def sum_array(arr:list):
#     if len(arr)<2 or arr==[]:
#         return 0
#     arr.sort()
#     arr.pop(0)
#     arr.pop(-1)
#     return sum(arr)
# print(sum_array([6, 2, 1, 8, 10]))

# def monkey_count(n):
#     a=[]
#     i=0
#     while i!=n:
#         i+=1
#         a.append(i)
#     return a
# print(monkey_count(5))

# def monkey_count(n):
#     a=[]
#     for i in range(1,n+1):
#         a.append(i)
#     return a

# print(monkey_count(5))