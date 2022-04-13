'''6. Пользователь вводит номер буквы в алфавите. Определить,
какая это буква.'''
number = int(input('Введите цифру не больше 26 : '))
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(f'Буква под номером {number}: {abc_list[number - 1]}')







