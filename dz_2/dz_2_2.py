# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

odd = 0
even = 0
for num in input('Введите целое число: '):
    if int(num) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'{odd} нечетных и {even} четных цифр')







