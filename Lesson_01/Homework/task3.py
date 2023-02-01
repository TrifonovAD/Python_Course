# 3. Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5 = 9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# in
# 385916
# out
# yes

# in
# 123456
# out
# no

# Вариант 1:

ticket_number = input('Введите номер билета\n')
sum_1 = int(ticket_number[0])+int(ticket_number[1])+int(ticket_number[2])
sum_2 = int(ticket_number[3])+int(ticket_number[4])+int(ticket_number[5])
print('Lucky!' if sum_1 == sum_2 else 'no')

# Вариант 2:

ticket_number = int(input('Введите номер билета\n'))
length_digit = len(str(ticket_number))
sum_1 = 0
sum_2 = 0
count = length_digit - 3
while length_digit:
    if length_digit > count:
        sum_1 += ticket_number % 10
    else:
        sum_2 += ticket_number % 10
    ticket_number //= 10
    length_digit -= 1

print('Lucky!' if sum_1 == sum_2 else 'no')
