"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from timeit import Timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(0, len(nums)) if nums[i] % 2 == 0]  # генератор быстрее цикла
    # по факту замеров, генератор быстрее на 4-3%


t1 = Timer("func_1([1,2,3,4,5,6,7,8,9,10,11,12])", "from __main__ import func_1")
print("func_1 ", t1.timeit(number=10000000), "milliseconds")
t1 = Timer("func_2([1,2,3,4,5,6,7,8,9,10,11,12])", "from __main__ import func_2")
print("func_2 ", t1.timeit(number=10000000), "milliseconds")
print(func_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(func_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
