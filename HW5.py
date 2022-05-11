from utils import *


"""
TASK 1
Напишите функцию calculations () так, чтобы она могла принимать две переменные и вычислять их сложение и вычитание. А также он должен возвращать как сложение, так и вычитание за один вызов возврата.
"""


def calculations(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction


calculations(random_number(), random_number())


"""
TASK 2
Напишите функцию Python для суммирования всех чисел в списке.
"""


def list_sum(a):
    return sum(a)


list_sum(random_number_list())


"""
TASK 3
Напишите функцию func () так, чтобы она могла принимать аргументы переменной длины и выводить все значения аргументов с индексом аргумента.
"""


def func(*args):
    return enumerate(list(args[0]))


func(random_list())


"""
TASK 4
Создайте функцию showEmployee () таким образом, чтобы она принимала имя сотрудника и его зарплату и отображала и то, и другое. Если в вызове функции отсутствует зарплата, присвойте зарплате значение по умолчанию 9000.
"""


def showEmployee(name, salary):
    default_salary = 9000
    if salary is None:
        return name, default_salary
    else:
        return name, salary


showEmployee(random_string(), random_number()*1000)


"""
TASK 5
Дано натуральное число N. Вычислите сумму его цифр. Напишите рекурсивную функцию
"""


def recursive_sum(N):
    if N <= 1:
        return N
    return N + recursive_sum(N - 1)


recursive_sum(random_number())


"""
TASK 6
Напишите рекурсивную функцию для вычисления числа Фибоначи
"""


def recursive_Fibonacci(n):
    if n < 3:
        return 1
    return recursive_Fibonacci(n - 1) + recursive_Fibonacci(n - 2)


recursive_Fibonacci(random_number())


"""
TASK 7
Напишите функцию для умножения всех чисел в списке. Рекурсивно
"""


def recursive_multiply_list(n, mult):
    if len(n) >= 1:
        mult = mult * n[0]
        recursive_multiply_list(n[1:], mult)
    else:
        return mult


recursive_multiply_list(random_number_list(), mult=1)


"""
TASK 8
Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае. 8 - YES, 3 - NO
"""


def is_number_exact_power_of_two(N):
    print(f"{N} is_number_exact_power_of_two")
    if (N == 0):
        print("NO")
        return False
    while (N != 1):
        if (N % 2 != 0):
            print("NO")
            return False
        N = N // 2
    print("YES")


is_number_exact_power_of_two(random_number()*random_number())


"""
TASK 9
Создайте inner функцию для вычисления сложения следующим образом:
Создайте внешнюю функцию, которая будет принимать два параметра, a и b
Создайте внутреннюю функцию внутри внешней функции, которая будет вычислять сложение a и b
Наконец, внешняя функция добавит 5 и вернет ее.
"""


def outer(a, b):
    def inner():
        add = a + b
        return add
    return inner() + 5


outer(random_number(), random_number())