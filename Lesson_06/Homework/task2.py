# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# # -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
# # 5
# # 15
# # [1, 9, 13, 14, 19]

mass = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_diap = int(input())
max_diap = int(input())
mass_index = []
for i in range(len(mass)):
    if min_diap <= mass[i] <= max_diap:
        mass_index.append(i)
print(*mass_index)