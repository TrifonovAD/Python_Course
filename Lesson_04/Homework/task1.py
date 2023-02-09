import random
n, m = int(input()), int(input())
list_1 = [random.randint(1, 20) for i in range(n)]
list_2 = [random.randint(1, 20) for i in range(m)]
print(*list_1, sep=', ')
print(*list_2, sep=', ')
new_list = sorted (list(set(list_1) & set(list_2)))
print(new_list if new_list else 'Совпадений нет')