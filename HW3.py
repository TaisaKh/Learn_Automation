from utils import *

"""
TASk 1
Посмотреть видео и создать проект на github https://www.youtube.com/watch?v=IH0W5bm4orc
Done - https://github.com/TaisaKh/Learn_Automation/tree/master
"""


"""
TASK 2
Напишите программу Python, которая принимает слово от пользователя и переворачивает его Пример: input - Hello Worlds output - sdlroW olleH 
"""
def revert_word1():
    word = random_string()
    word_length = - len(word)
    word_to_list = []
    list_index = -1
    result = ""
    for item in word:
        word_to_list.append(item)
    while list_index != word_length - 1:
        tmp = (word_to_list[list_index])
        list_index -= 1
        result = result + tmp
    return result


revert_word1()


def revert_word2():
    word = random_string()
    return word[::-1]


revert_word2()


"""
TASK 3
Напишите программу Python для построения следующего шаблона, используя вложенный цикл for.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
def triangle():
    height = random_number()
    print(f"Random height of triangle is: {height}")
    half_height = int(height / 2)
    peak = half_height
    if height % 2 != 0:
        peak = half_height + 2
    else:
        peak += 1
    for x in range(peak):
        print("*" * x)
        x += 1
    for z in range(peak):
        print("*" * half_height)
        half_height -= 1


triangle()


"""
TASK 4
Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке 
убывания если A > B
"""
def counting():
    a = random_number()
    b = random_number()
    numbers = []
    if a > b:
        for i in range(b, a + 1):
            numbers.append(i)
            i += 1
        return sorted(numbers, reverse=True)
    else:
        for i in range(a, b + 1):
            numbers.append(i)
            i += 1
        return numbers


counting()


"""
TASK 5
Даны два целых числа A и B (при этом A < B). Выведите все числа от A до B включительно. 
"""
def comparing():
    a = random_number()
    print(f"a: {a}")
    b = random_number()
    print(f"b: {b}")
    while b < a:
        b = random_number()
        print(f"new b: {b}")

    for i in range(a, b + 1):
        print(i)
        i += 1


comparing()


"""
TASK 6
Напишите программу, которая удаляет дубликаты элементов из списка.
"""
def delete_duplicates_from_list():
    return list(dict.fromkeys(random_number_list()))


delete_duplicates_from_list()


"""
TASK 7
Напишите программу, которая копирует список
"""
import copy


def list_copy():
    return copy.deepcopy(random_list())


list_copy()


"""
TASK 8
Напишите программу, которая находит разницу между двумя списками и сохраняет ее в новый список. Вывести результат на экран. 
"""
def difference_between_lists():
    return list(set(random_list()) ^ set(random_list()))


difference_between_lists()


"""
TASK 9
Напишите программу для объединения следующих словарей для создания нового
Исходные словари :

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

Результат : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
def combining_dictionaries():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    return {**dic1, **dic2, **dic3}


combining_dictionaries()


"""
TASK 10
Напишите программу, которая выводит словарь, в котором ключи представляют собой числа от 1 до 15 (оба включены), а значения представляют собой квадраты ключей. Генерация ключей и значений должна быть выполнена через цикл. 
"""
def square_number_dictionary():
    dictionary = {}
    for number in range(1, 16):
        dictionary[number] = number*number
        number += 1
    return dictionary


square_number_dictionary()

