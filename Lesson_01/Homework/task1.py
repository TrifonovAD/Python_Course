# 1. Найдите сумму цифр трехзначного числа.
# in
# 123

# out
# 6

# Вариант 1.

number = input('Введите трехзначное число\n')
print(f'Cумма цифр {int (number[0])+int (number[1])+int (number[2])}')

# Вариант 2.

number = int(input('Введите число\n'))
sum_digit = 0
while number:
    sum_digit += number % 10
    number //= 10
print(f'Cумма цифр {sum_digit}')

# Вариант 3.

number = input('Введите число\n')
sum = 0
for digit in number:
    sum += int(digit)
print(f'Cумма цифр {sum}')
