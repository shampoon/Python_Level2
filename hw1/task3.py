def most_proceed1(company_dict):
    most_company_list = []
    for k in range(1, 4):  # 4
        for key, val in company_dict.items():       # O(4*n)
            hi_value = 1
            for val2 in company_dict.values():      # O(4*n*n)
                if val < val2:                      #  O(1)
                    hi_value = 0                    #  O(1)
            if hi_value:
                most_company_list.append(key)       #  O(1)
        company_dict.pop(most_company_list[k - 1])  #  O(1)
    return most_company_list
    """ Итоговая сложность алгоритма O(4n^2)
    """


def most_proceed2(company_list, proceed_list):
    most_company_list = [company_list[proceed_list.index(max(proceed_list))]]       # O(n)
    proceed_list[proceed_list.index(max(proceed_list))] = 0                         # O(n)
    most_company_list.append(company_list[proceed_list.index(max(proceed_list))])   # O(n)
    proceed_list[proceed_list.index(max(proceed_list))] = 0                         # O(n)
    most_company_list.append(company_list[proceed_list.index(max(proceed_list))])   # O(n)
    return most_company_list
    """ Итоговая сложность алгоритма O(3n). нужно брать максимальное число, в этом случае это O(n), 
    но это формат записи. Можно ведь тот же смысл заложить в цикл fro i in range (1, 4), тогда получится сложность 
    O(3*n). Поэтому пишу сложность именно O(3*n), а не O(n)
    """

    """Второй метод эффективнее, т.к. первый метод O(n^2), а это медленнее O(n)"""

print('++++++++++++++ First method ++++++++++++++')
d = {'Company1': 10, 'Company2': 120, 'Company3': 15, 'Company4': 170, 'Company5': 30, 'Company6': 140,
     'Company7': 50, 'Company8': 110, 'Company9': 55, 'Company10': 80, 'Company11': 100, 'Company12': 20}
print(most_proceed1(d))

print('++++++++++++++ Second method ++++++++++++++')
company_list = ['Company1', 'Company2', 'Company3', 'Company4', 'Company5', 'Company6', 'Company7', 'Company8',
                'Company9', 'Company10', 'Company11', 'Company12']
company_proceeds = [10, 120, 15, 170, 30, 140, 50, 110, 55, 80, 100, 20]
print(most_proceed2(company_list, company_proceeds))
