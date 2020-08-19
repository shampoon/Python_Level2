from collections import defaultdict
from collections import Counter

manufact_cnt = int(input('Введите количество предприятий для расчета прибыли: '))
d = defaultdict(int)
summ_profit = 0
for i in range(manufact_cnt):
    manufact_name = input('Введите название предприятия: ')
    profit_list = list(map(int, input('через пробел введите прибыль данного предприятия'
                                      ' за каждый квартал(Всего 4 квартала): ').split(' ')))
    profit = sum(profit_list)
    summ_profit = summ_profit + profit
    d[manufact_name] += profit
midle_profit = summ_profit / manufact_cnt
res_low = []
res_high = []
for manuf, prof in d.items():
    if prof < midle_profit:
        res_low.append(manuf)
    else:
        res_high.append(manuf)
print(f'Средняя годовая прибыль всех предприятий: {midle_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {res_high}')
print(f'Предприятия, с прибылью ниже среднего значения: {res_low}')

