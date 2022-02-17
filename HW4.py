from utils import *


"""
TASK1
Напишите программу для преобразования списка в кортеж
"""
def list_to_tuple():
    return tuple(random_list())


list_to_tuple()


"""
TASK 2
Напишите программу для замены последнего значения
кортежей в списке
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""
def change_last_tuple_element():
    sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    new_list = []
    for item in sample_list:
        new_list.append(list(item))
    for i in range(len(sample_list)):
        new_list[i][-1] = 100
    return tuple(new_list)


change_last_tuple_element()


"""
3. Напишите программу для поэлементного вычисления суммы
заданных кортежей. Результатом должен быть кортеж.
Input
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Output
(6, 9, 8, 6)
"""
def sum_elements_in_tuple():
    original_tuple = ((1, 2, 3, 4), (3, 5, 2, 1), (2, 2, 3, 1))
    return tuple(map(sum, zip(original_tuple[0], original_tuple[1], original_tuple[2])))


sum_elements_in_tuple()


"""
TASK 4
Напишите программу, которая проверяет, присутствует ли А в
наборе или нет. А вводится с клавиатуры
"""
def check_element_in_set_is_present():
    random_set = set(random_string())
    print(random_set)
    set_a = set(input("Please enter an 'A' to check if 'A' is in the set: "))
    if random_set & set_a:
        print(f"{set_a} is in the set")
    else:
        print(f"{set_a} is not in the set")


check_element_in_set_is_present()


"""
TASK 5
Напишите программу, чтобы проверить, не имеют ли два
заданных набора (set) общих элементов.
"""
def common_elements_in_set():
    set_x = set(random_number_list())
    set_y = set(random_number_list())
    return set_x & set_y


common_elements_in_set()


"""
TASK 6
Напишите программу для поиска элементов в данном наборе A (set), которых нет в другом наборе B.
"""
def difference_in_set_a():
    set_a = set(random_number_list())
    set_b = set(random_number_list())
    return set_a.difference(set_b)


difference_in_set_a()


"""
TASK 7
Напишите программу, которая удаляет пересечение 2-го набора из 1-го набора.
"""
def delete_same_elements():
    set_a = set(random_number_list())
    set_b = set(random_number_list())
    set_intersection = set_a & set_b
    for item in set_intersection:
        if item in set_intersection:
            set_a.remove(item)
    return set_a


delete_same_elements()


"""
TASK 8
Реализовать логику Union для двух списков (list), проверить работу алгоритма на set.union
"""
list_a = random_number_list()
list_b = random_number_list()
def union_lists():
    list_sum = list_a + list_b
    union_list = []
    for x in list_sum:
        if x not in union_list:
            union_list.append(x)
    return (sorted(union_list))


def check_union_lists():
    if set(union_lists()) == set().union(list_a, list_b):
        print(f"union_lists: {union_lists()} and set_union: {set().union(list_a, list_b)} are equal")


check_union_lists()


"""
TASK 9
Реализовать логику Difference для двух списков (list), проверить работу алгоритма на set.difference
"""
list_number_a = random_number_list()
list_number_b = random_number_list()
def difference_lists():
    list_difference = []
    for item in list_number_a:
        if item not in list_number_b:
            if item in list_difference:
                continue
            list_difference.append(item)
    return sorted(list_difference)


difference_lists()


def check_difference_lists():
    set_a = set(list_number_a)
    set_b = set(list_number_b)
    set_difference = set_a.difference(set_b)
    if set(difference_lists()) == set_difference:
        print(f"list_difference: {difference_lists()} and set_difference: {set_difference} are equal")


check_difference_lists()