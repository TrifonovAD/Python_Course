# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

number = int(input())
first_number = 0
second_number = 1
index = 1
flag = False
while number >= second_number:
    if number == second_number:
        flag = True
    first_number, second_number = second_number, first_number + second_number
    index +=1    
print(index if flag else '-1')