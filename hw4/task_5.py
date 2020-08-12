"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
# решето в разы быстрее


from timeit import Timer


def simple(i):  # сложность O(n^2)
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:   # O(n)
        t = 1
        is_simple = True
        while t <= n:   # тут становится O(n * n)
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def difficult(num):  # итоговая сложность O(log n * n^2 / 80)
    # список заполняется значениями от 0 до n
    n = num * 2
    while True:  # O(log n)
        a = [i for i in range(n + 1)]  # добавляется O(n)
        a[1] = 0
        i = 2
        while i <= n:   # O(n/2)
            if a[i] != 0:
                j = i + i
                while j <= n:   # O(n/4)
                    a[j] = 0
                    j = j + i
            i += 1
        a = set(a)
        a.remove(0)
        a = list(a)
        a.sort()
        print(n)
        if len(a) < num:
            n = n * 2
        else:
            break
    return a[num - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
r, n = 10, 100
t1 = Timer("simple(10)", "from __main__ import simple")
print("simple(10) ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

t1 = Timer("simple(100)", "from __main__ import simple")
print("simple(100) ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

t1 = Timer("simple(1000)", "from __main__ import simple")
print("simple(1000) ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

t1 = Timer("difficult(10)", "from __main__ import difficult")
print("difficult(10) ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

t1 = Timer("difficult(100)", "from __main__ import difficult")
print("difficult(100) ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

t1 = Timer("difficult(1000)", "from __main__ import difficult")
print("difficult(1000) ", min(t1.repeat(repeat=r, number=n)), "milliseconds")

print(simple(i))
print(difficult(i))
