# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3


# Вариант 1. Находим решение перебором всех натуральных чисел от 1 до 1000.

summa_number = int(input('Введите сумму чисел: '))
proizv_number = int(input('Введите произведение чисел: '))
flag = False
for i in range(1, 1001):
    for j in range(1, 1001):
        if (i+j == summa_number and i * j == proizv_number) and flag == False:
            print(i, j)
            flag = True
if flag == False:
    print('Нет решения')

# Вариант 2. Находим решение через дискриминант.

summa_number = int(input('Введите сумму чисел: '))
proizv_number = int(input('Введите произведение чисел: '))
discriminant = summa_number ** 2 - 4 * proizv_number
if discriminant == 0:
    result_a = result_b = summa_number / 2
else:
    result_a = ((summa_number - discriminant ** 0.5)/2)
    result_b = ((summa_number + discriminant ** 0.5)/2)
print(int(result_a), int(result_b))
