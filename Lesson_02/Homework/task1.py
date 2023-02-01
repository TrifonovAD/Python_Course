# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

count_coin = int(input('Количество монет?\n'))
heads_count = tails_count = 0
print('Орел (1), решка (0)')

for i in range(count_coin):
    coin_stat = int(input())
    if coin_stat == 1:
        heads_count += 1
    else:
        tails_count += 1
print(heads_count if heads_count < tails_count else tails_count)
