# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

som_array = [random.randint(0, 101) for i in range(10)]
print(f'Массив из десяти случайных чисел: {som_array}')

max_item = som_array[0]
min_item = som_array[0]

for i in som_array:
    if i > max_item:
        max_item = i
    elif i < min_item:
        min_item = i
min_index = som_array.index(min_item)
max_index = som_array.index(max_item)
som_array[min_index], som_array[max_index] = som_array[max_index], som_array[min_index]
print(f'В массиве поменяли местами минимальный и максимальный элементы: {som_array}')