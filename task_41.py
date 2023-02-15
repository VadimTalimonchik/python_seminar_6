# Задача 41.
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве.Далее записаны N чисел — элементы
# массива. Массив состоит из целых чисел.
# Ввод:           Ввод:
# 5 5
# 1 2 3 4 5       1 5 1 5 1
# Вывод:          Вывод:
# 0               2

# ----------------------------

# # вариант 1
# from random import randint

# list = [randint(0, 100) for i in range(int(input('N: ')))]
# print(list)

# count = 0
# for i in range(len(list)):
#     if list[i - 2] < list[i - 1] > list[i]:
#         count += 1
# print(count)

# -------------------------------

# # вариант 2
# from random import randint

# n = int(input('Введите количество элементов: '))
# list = []
# for i in range(n):
#     list.append(randint(1, 10))
# print(list)

# count = 0
# for i in range(len(list)):
#     if list[i - 1] < list[i] > list[i + 1]:
#         count += 1
# print(count)

# -----------------------------

# # вариант 3
# from random import randint
# num_list = [randint(1, 20) for _ in range(int(input('Введите размер массива: ')))]
# print(*num_list)

# for i in range(1, len(num_list) - 1):
#     if num_list[i -1] < num_list[i] and num_list[i + 1] < num_list[i]:
#         print(num_list[i - 1], num_list[i], num_list[i + 1], end = ' ')

# -----------------------------

# # вариант 4
# import random

# str1 = [random.randint(1, 10) for i in range(int(input('Введите число: ')))]

# c = 0
# for i in range(1, len(str1) - 1):
#     if str1[i] > str1[i - 1] and str1[i] > str1[i + 1]: c += 1
#     # if str1[-1] > str1[0] and str1[-1] > str1[-2]: c += 1
#     # if str1[0] > str1[-1] and str1[0] > str1[1]: c += 1

# print(str1)
# print(c)

# -----------------------------

# вариант 5
from random import randint
arr = [randint(1, 10) for i in range(int(input('enter n = ')))]
count = 0
print(*arr)

for i in range(len(arr)):
    if arr[i - 1] < arr[i] > arr[(i + 1) % len(arr)]:
        count += 1
print(count)
