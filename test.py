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
# print('n'.join('1'*3))

N = int(input())
M = int(input())
T = int(input())
print(f'{((((M+T) // 60) + N)%24):02}:{((M + (T % 60)) % 60):02}')