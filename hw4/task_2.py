"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
from timeit import Timer
import random


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


def recursive_reverse1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse1(number // 10)}'

# замеры мемоизированной функции в разы улучшаются, если в замерах вызывать функцию со статичным аргументом
# т.к. в замере производятся вызов функции с одним и тем же аргументом 1000 раз, функция вычисляется
# только на первом вызове, остальные 999 раз из кэша берется рассчитанное значение функции
# =============================================================================================================
# но ситуация изменяется в худшую сторону, если в качестве агрумента вызывать рандомное число
# мемоизированная функция начинает работать медленнее чем не мемоизированная


@memorize
def recursive_reverse2(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse2(number // 10)}'


# метод преобразования в строку и разворот чемпион, если производить замеры с рандомным аргументом
def recursive_reverse3(number):
    return int(str(number)[::-1])  # быстрый вариант - преобразовать в строку и развернуть ее


n = 1000
r = 100
t1 = Timer("recursive_reverse1(randint(100000000, 900000000))", """from __main__ import recursive_reverse1
from random import randint""")
print("recursive_reverse1 - no memorize         ", min(t1.repeat(repeat=r, number=n)), "milliseconds")
print(recursive_reverse1(random.randint(100000000, 900000000)))

t1 = Timer("recursive_reverse2(randint(100000000, 900000000))", """from __main__ import recursive_reverse2
from random import randint""")
print("recursive_reverse2 - memorize mode       ", t1.timeit(number=n), "milliseconds")
print(recursive_reverse2(random.randint(100000000, 900000000)))

t1 = Timer("recursive_reverse3(randint(100000000, 900000000))", """from __main__ import recursive_reverse3
from random import randint""")
print("recursive_reverse3 - string reverce mode ", t1.timeit(number=n), "milliseconds")
print(recursive_reverse3(random.randint(100000000, 900000000)))
