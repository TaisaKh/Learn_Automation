"""
TASK 1
За день машина проезжает n километров.
Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Программа получает на вход числа n и m.
"""
def time_for_trip(n, m):
    days = int(m/n)
    speed = n / 24
    t = m / speed
    hours = format(t % 24, '.2f')
    print(f"{days} days and {hours} hours you need to move for {m} km with speed {n} km per day.")


time_for_trip(83, 345)


"""
TASK 2
Пользователь вводит трехзначное число. Найдите сумму его цифр. (используйте %)
"""
def numbers_sum(number):
    number_to_list = [int(a) for a in str(number)]
    total = sum(number_to_list)
    print(f"{total} is the sum of numbers in {number}")


numbers_sum(324)


"""
TASK 3
Найти максимальное число из трех. Числа вводится с клавиатуры
"""
def max_number(number1, number2, number3):
    number1 = int(input("Please input number 1: "))
    number2 = int(input("Please input number 2: "))
    number3 = int(input("Please input number 3: "))
    if number1 > number2 and number1 > number3:
        print(f"{number1} is the biggest number.")
    elif number2 > number3:
        print(f"{number2} is the biggest number.")
    else:
        print(f"{number3} is the biggest number.")


max_number(123, 345, 343)


"""
TASK 4
Определить високосный год или нет.Число вводится с клавиатуры
"""
def leap_year(year):
    year = int(input("Please enter a year to know if it is a leap year or not: "))
    div_by_4 = year % 4 == 0
    div_by_100 = year % 100 == 0
    div_by_400 = year % 400 == 0
    if div_by_400 and div_by_100:
        print(f"{year} is a leap year.")
    elif div_by_4 and div_by_100 is False:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


leap_year(1346)


"""
TASK 5
Определить четное или нечетное число. Число вводится с клавиатуры
"""
def even_or_odd_number(even_or_odd_number):
    even_or_odd_number = int(input("Please enter a number: "))
    if even_or_odd_number % 2 == 0:
        print(f"{even_or_odd_number} is an even number.")
    else:
        print(f"{even_or_odd_number} is an odd number.")


even_or_odd_number(234)


"""
TASK 6
Найти корни квадратного уравнения и вывести их на экран, если они есть. 
Если корней нет, то вывести сообщение об этом. 
Конкретное квадратное уравнение определяется коэффициентами a, b, c, которые вводит пользователь.
"""
import math
def quadratic_equation(coefficient_a, coefficient_b, coefficient_c):
    coefficient_a = int(input("Please enter a coefficient a: "))
    coefficient_b = int(input("Please enter a coefficient b: "))
    coefficient_c = int(input("Please enter a coefficient c: "))
    discriminant = coefficient_b ** 2 - 4 * coefficient_a * coefficient_c
    discriminant_sqrt = math.sqrt(discriminant)
    root1 = (-coefficient_b + discriminant_sqrt) / 2 * coefficient_a
    root2 = (-coefficient_b - discriminant_sqrt) / 2 * coefficient_a
    if discriminant < 0:
        print(f"Discriminant is {discriminant}. There is no root")
    elif discriminant == 0:
        print(f"Discriminant is {discriminant}. There is only one root. x = {root1}")
    else:
        print(f"Discriminant is {discriminant}. There are two roots. x1 = {root1} and x2 = {root2}")


quadratic_equation(1, 2, 3)


"""
TASK 7
Дана следующая функция y=f(x):
y = 2x – 10, если x > 0
y = 0, если x = 0
y = 2 * |x| – 1, если x < 0
Найти значение функции по x, который вводиться с клавиатуры
"""
def function(x_value):
    x_value = int(input("Please enter X: "))
    if x_value > 0:
        y = (2 * x_value) - 10
        print(f"y = {y}")
    elif x_value == 0:
        print("y = 0")
    else:
        y = (2 * abs(x_value)) - 1
        print(f"y = {y}")


function(1)
