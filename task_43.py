# Задача 43.
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.
# Ввод:           Вывод:
# 1 2 3 2 3       2

# -----------------------------

# # вариант 1
from random import randint

list = [randint(0, 10) for i in range(int(input('N: ')))]
print(list)
k = 0

for i in range(len(list) - 1):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            k += 1
print(k)

# -----------------------------

# # вариант 1
# list = [10, 8, 10, 4, 8, 4, 8, 10, 4, 4, 4]
# count = 0

# for i in list:
#     last_element = list.pop()
#     if last_element in list:
#         list.remove(last_element)
#         count += 1
# print(count)
