'''6. Пользователь вводит номер буквы в алфавите. Определить,
какая это буква.'''
number = int(input('Введите цифру не больше 26 : '))
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(abc_list)
if number <= len(abc_list):
    print(f'Буква под номером {number}: {abc_list[number - 1]}')
else:
    print(
      f'Введено число превышающее количество букв в алфавите ({len(abc_list)})'
    )






