import random
import os
os.system('cls')
n = int(input())
my_list = [random.randint(1, n) for i in range(n)]
print(*my_list)
x = int(input())
print(my_list.count(x))
