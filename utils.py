import random
import string


def random_number():
    random_number = random.randint(0, 10)
    return random_number


def random_number_list():
    random_number_list = []
    for _ in range(0, random_number()):
        random_number_list.append(random.randint(0, random_number()))
    return random_number_list


def random_letter():
    random_letter = random.choice(string.ascii_letters)
    return random_letter


def random_string():
    random_string = "".join((random_letter()) for _ in range(random_number()))
    return random_string


def random_list():
    random_list = []
    for _ in range(random_number()):
        random_list.append(random_string() or random_number())
    return random_list

