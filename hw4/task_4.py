"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

# так и не получилось у меня написать версию быстрее...все +/- одинаково выполняются

from timeit import Timer

array = [1, 3, 1, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 4, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    count2 = [array.count(el) for el in array]
    return f'Чаще всего встречается число {array[count2.index(max(count2))]}, ' \
           f'оно появилось в массиве {max(count2)} раз(а)'


def func_4():
    count2 = {array.count(el): el for el in array}
    return f'Чаще всего встречается число {count2.get(max(count2.keys()))}, ' \
           f'оно появилось в массиве {max(count2.keys())} раз(а)'


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def get_count(i):
    return array.count(i)


def func_5():
    m = 0
    num = 0
    for i in array:
        count = get_count(i)  # array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


r, n = 100, 1000000
t1 = Timer("func_1", "from __main__ import func_1")
print("func_1 ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

t1 = Timer("func_2", "from __main__ import func_2")
print("func_2 ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

t1 = Timer("func_3", "from __main__ import func_3")
print("func_3 ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

t1 = Timer("func_4", "from __main__ import func_4")
print("func_4 ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

t1 = Timer("func_5", "from __main__ import func_5")
print("func_5 ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())