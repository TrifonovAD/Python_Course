# 1 Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

# Вариант 1

n = int(input('Количество элементов массива: '))
my_list = [int(input(f'{i+1}-й элемент: ')) for i in range(n)]
x = int(input('Искомое число: '))
print(*my_list)
result = sum(x == list_elements for list_elements in my_list)
print(f'Число {x} встречается {result} раз(а)')

# Вариант 2

my_list = [int(i)
            for i in input('Введите элементы массива через пробел: ').split()]
x = int(input('Искомое число: '))
print(f'Число {x} встречается {my_list.count(x)} раз(а)')