# 1.В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.


diver = dict.fromkeys(range(2, 10), 0)
for n in range(2, 100):
    for i in range(2, 10):
        if n % i == 0:
            diver[i] += 1

for key in diver:
    print(f'числу {key} кратны {diver[key]} чисел')