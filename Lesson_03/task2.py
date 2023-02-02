list_nums = [1, 2, 3, 4, 5]
k = 2

print(list_nums)

for i in range(k - 1):
    list_nums.insert(0, list_nums.pop(- 1))

print(k, list_nums)