# 4. Определить, какое число в массиве встречается чаще всего.

import random

som_array = [random.randint(0, 101) for i in range(30)]
print(f'Мой масив: {som_array}')
counter = 0
for num in som_array:
    if som_array.count(counter) < som_array.count(num):
        counter = som_array.index(num)
print(f'{som_array[counter]}, встречается чаще всего. {som_array.count(counter)} раз')



