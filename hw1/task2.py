import random


def first_method(num_list):
    for i in range(0, len(num_list)):
        bigger_count = 0
        for j in range(0, len(num_list)):
            if num_list[i] < num_list[j]:
                bigger_count += 1
        if bigger_count == (len(num_list) - 1):
            return num_list[i]


def second_method(num_list):
    min_value = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] < min_value:
            min_value = num_list[i]
    return min_value


my_list = [random.randint(0, 100) for i in range(10)]
print(my_list)
print(f'First method result: {first_method(my_list)}')
print(f'Second method result: {second_method(my_list)}')
