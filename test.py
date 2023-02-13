# import random
# import os
# os.system('cls')
# n = int(input())
# my_list = [random.randint(1, n) for i in range(n)]
# print(*my_list)
# x = int(input())
# print(my_list.count(x))
'''
<string>.split (sep, maxsplit) разбивает исходную строку <string> по вхождениям разделителя sep, maxsplit раз.
<sep>.join(<iterable>) объединяет подстроки в итерируемый объект <iterable>, используя <sep> в качестве разделителя.
'''

# n = int(input())
# print('\n'.join({n}*3))


# x = 'текст выравнивается по правому краю'

# # Без заполнителя `fillchar`
# print(x.rjust(len(x)+20))
# # '                    текст выравнивается по правому краю'

# print(x.rjust(len(x)+20, '*'))
# # '********************текст выравнивается по правому краю'

# # Ширина `width` меньше длины центрируемой строки
# print(x.rjust(len(x)-10, '*'))
# # 'текст выравнивается по правому краю'

# # x.rjust()
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # TypeError: rjust() takes at least 1 argument (0 given)

# def addList(length):
#     t_list = [int(input()) for i in range(length)]
#     return t_list

"""
n = int(input())
my_list1 = [int(input()) for i in range(n)]
m = int(input())
my_list2 = [int(input()) for i in range(m)]

list_diff = []

for i in my_list1:
    if i not in my_list2:
        list_diff.append(i)
        
print(*list_diff)
"""

n = int(input())
my_list1 = [int(input()) for i in range(n)]
min_count = 0
for i in range(1, len(my_list1)-1):
    if (my_list1[i] > my_list1[i-1]) and (my_list1[i] > my_list1[i+1]):
        min_count += 1
print(min_count)

'''
Задача №1461. Шарики 
В одной компьютерной игре игрок выставляет в линию шарики разных цветов. 
Когда образуется непрерывная цепочка из трех и более шариков одного цвета, она удаляется из линии. 
Все шарики при этом сдвигаются друг к другу, и ситуация может повториться. 
Напишите программу, которая по данной ситуации определяет, сколько шариков будет "уничтожено". 
Естественно, непрерывных цепочек из трех и более одноцветных шаров в начальный момент 
может быть не более одной. 
 
Входные данные 
   Сначала вводится количество шариков в цепочке (не более 1000) и цвета шариков (от 0 до 9, каждому цвету соответствует свое целое число). 
Выходные данные 
   Требуется вывести количество шариков, которое будет "уничтожено". 
Примеры 
   входные данные 
   5 1 3 3 3 2
   Выходные данные
   3
'''