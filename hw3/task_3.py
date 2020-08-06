import hashlib

substrings = set()
S = 'papa'

for i in range(0, len(S)):
    for j in range(i + 1, len(S) + 1):
        if not (i == 0 and j == (len(S))):
            substrings.add(hashlib.sha256(S[i:j].encode('utf-8')).hexdigest())
print(f'Количество подстрок: {len(substrings)}')


"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
