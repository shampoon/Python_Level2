"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
# Вывод: эффективнее третья реализация
import cProfile
from timeit import Timer


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
        return revers_num


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    for i in range(1000):
        revers(12345689988)
    for i in range(1000):
        revers_2(12345689988)
    for i in range(1000):
        revers_3(12345689988)


r, n = 100, 1000
t1 = Timer("revers(12345689988)", "from __main__ import revers")
print("revers ", min(t1.repeat(repeat=r, number=n)), "milliseconds")
print(revers(12345689988))

t1 = Timer("revers_2(12345689988)", "from __main__ import revers_2")
print("revers_2 ", min(t1.repeat(repeat=r, number=n)), "milliseconds")
print(revers_2(12345689988))

t1 = Timer("revers_3(12345689988)", "from __main__ import revers_3")
print("revers_3 ", min(t1.repeat(repeat=r, number=n)), "milliseconds")
print(revers_3(12345689988))

cProfile.run('main()')