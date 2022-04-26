# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

'''3_5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.'''


# реализация № 1
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

# реализация № 2

def func(array):
    new_list = [i for i in array if i < 0]
    maximum = max(new_list)
    idx = new_list.index(maximum)