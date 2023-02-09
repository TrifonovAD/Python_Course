# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# 8
# 5 4 2 2 4 2 2 5


def max_to_min(list):
    num_min = min(list)
    num_max = max(list)
    return [num_min if i == num_max else i for i in list]


print(*max_to_min([int(i) for i in input().split()]))
