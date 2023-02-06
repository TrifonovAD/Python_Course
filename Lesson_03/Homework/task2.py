# 2 Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу num. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в массиве. 
# В последующих строках # записаны N целых чисел Ai. 
# Последняя строка содержит число num

# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5


n = int(input('Количество элементов массива: '))
str_mass = input('Введите элементы массива через пробел: ')
my_list = [int(i) for i in str_mass.split()]
num = int(input('Задайте число: '))
find_number = my_list[0]
find_number_2 = '\b\b\b'
for i in range(1, len(my_list)):
    if abs(num - my_list[i]) < abs(num - find_number):
        find_number = my_list[i]
    if (abs(num - my_list[i]) == abs(num - find_number) and
            find_number != my_list[i]):
        find_number_2 = my_list[i]
print(f'Ближайший элемент по величине: {find_number} и {find_number_2}')
