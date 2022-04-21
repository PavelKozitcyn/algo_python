'''5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.'''
import random

som_array = [random.randint(-8, 101) for i in range(30)]
print(f'Мой масив: {som_array}')
min_element = 0
for num in som_array:
    if som_array[min_element] > num:
        min_element = som_array.index(num)
if som_array[min_element] >= 0:
    print('Все эдементы положительные.')
else:
    print(f'Mаксимальный отрицательный элемент - {som_array[min_element]}, позиция {min_element}')


