# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

count_watermelon = int(input('Количество арбузов:\n'))

for i in range(count_watermelon):
    weight = int(input())
    if i == 0:
        max_weight = min_weight = weight
    else:
        if weight > max_weight:
            max_weight = weight
        elif weight < min_weight:
            min_weight = weight
print(min_weight, max_weight)
