import time


def list_method():
    user_list = [[f'user_ {i}', f'pwd_{i}'] for i in range(0, 1000000)]
    return user_list


def dict_method():
    users = {f'user_ {i}': f'pwd_{i}' for i in range(0, 1000000)}
    return users


def func_decorator(function_to_decorate):
    start_time = time.time()
    function_to_decorate()
    end_time = time.time()
    return end_time - start_time


"""словарь заполняется на 30-50% быстрее"""
print('Hello!')
print(f'Заполнение методом списка  заняло: {func_decorator(list_method)} c')
print(f'Заполнение методом словаря заняло: {func_decorator(dict_method)} c')

"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
