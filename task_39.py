# Задача 39.
# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут
# в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов
# в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива. (каждое число вводится с новой строки)
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12

# -----------------------

# # вариант 1 - как-то не совсем верно работает
# import random

# n = []
# m = []
# N = int(input('Введите количество цифр массива N: '))
# M = int(input('Введите количество цифр массива M: '))

# for i in range(N):
#     n.append(random.randint(1, 10))

# for i in range(M):
#     m.append(random.randint(1, 10))

# print(n)
# print(m)

# k = 0
# for i in range(N):
#     for j in range(M):
#         if(n[i] == m[j]):
#             k += 1
#         if k == 0:
#             print(n[i])
#         k = 0

# ---------------------------

# # вариант 2
# list1 = [int(input('add element: ')) for i in range(int(input('enter n = ')))]
# list2 = [int(input('add element: ')) for i in range(int(input('enter m = ')))]

# print([i for i in list1 if i not in list2])

# ------------------------

# # вариант 3
# a = int(input('Введите число элементов в первом списке: '))
# list_1 = []
# for i in range(a):
#     n = int(input('Введите число: '))
#     list_1.append(n)

# b = int(input('Введите число элементов в первом списке: '))
# list_2 = []
# for i in range(b):
#     m = int(input('Введите число: '))
#     list_2.append(m)

# print(list_1)
# print(list_2)

# k = 0
# for i in list_1:
#     for j in list_2:
#         if i == j:
#             k += 1
#     if k == 0:
#         print(i)
#     k = 0

# ---------------------------------

# вариант 4
from random import randint

num_list_1 = [randint(1, 10) for _ in range(int(input('Введите размер 1-го массива: ')))]
num_list_2 = [randint(1, 10) for _ in range(int(input('Введите размер 2-го массива: ')))]

print(*num_list_1)
print(*num_list_2)

list_unique_nums = set(num_list_1) - set(num_list_2)
for i in num_list_1:
    if i in list_unique_nums:
        print(i, end = ' ')
print()