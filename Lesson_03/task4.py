# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает
# количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)
# list_nums = [0, -1, 5, 2, 3]

# print(sum(i > j for i, j in zip(list_nums[1:], list_nums)))


list_nums = [0, -1, 5, 2, 3]
print (sum([list_nums[i]>list_nums[i-1] for i in range(1, len(list_nums))]))