# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

som_array = [random.randint(0, 101) for n in range(10)]
print(f'Мой масив: {som_array}')
min_element = som_array[0]
max_element = som_array[1]

for num, item in enumerate(som_array):
    print(num)
    if item <= min_element:
        min_element = item
        min_ind = num
    elif item >= max_element:
        max_element = item
        max_ind = num
print(f'Минимальный элемент = {min_element}(индекс {min_ind})\nМаксимальный элементам = {max_element} (индекс {max_ind})')
if max_ind < min_ind:
    max_ind, min_ind = min_ind, max_ind
print(f'Элементы между минимальным и максимальным: {som_array[min_ind + 1:max_ind]}')

som_sum = 0
for i in range(min_ind + 1, max_ind):
    som_sum += som_array[i]

print(som_sum)
