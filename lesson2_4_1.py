import random
import time
from functools import reduce

"""
Объявить две функции: 1 - принимает список чисел как аргумент и сортирует его по убыванию, 
2 - принимает список чисел как аргумент и сортирует его по возрастанию. 
Отсортировать список чисел по убыванию или по возрастанию, 
в зависимости от того что выберет пользователь.
 Реализовать с помощью функции, которая передается как аргумент
"""


def spisok_up_sort(spisok):
    return spisok.sort()


def spisok_down_sort(spisok):
    return spisok.sort(reverse=True)


def up_or_down(user_choece, funk1=spisok_up_sort, funk2=spisok_down_sort):
    spisok = random.sample(range(10), 10)
    if int(user_choece) == 1:
        funk1(spisok)
    else:
        funk2(spisok)
    return spisok


print(up_or_down(9))

"""
Написать функцию таймер, которая будет принимать функцию как аргумент и вычислять время выполнения этой функции.
"""


def timer(sum_funk):
    begin_time = time.time()
    print("sjdfn")
    sum_funk()
    end_time = time.time() - begin_time
    print("time for funk", end_time * 1000)


def sum_f():
    sum_big_list = list(range(1, 1000000))
    b = 0
    for i in sum_big_list:
        b += i


timer(sum_f)

"""
Создать функцию create_adder, внутри которой будет объявлена функция add_elems(list_of_elems)и будет возвращаться 
эта функция. Вызвать функцию create_adder и сложить несколько рандомных чисел 
(произвольное количество) с помощью add_elems.

"""


def create_adder():
    def add_elems(list_of_elems):
        sum_e = 0
        for elems in list_of_elems:
            sum_e += elems
        return sum_e

    return add_elems


elements = list(random.sample(range(10), 3))

cr_ad = create_adder()
print(cr_ad(elements))

"""
Написать функцию create_counter, в которой будет объявлена переменная counter и функция generate_password, 
вернуть функцию generate_password. Функция generate_password должна генерировать пароль и увеличивать counter на 1. 
Вызвать функцию для генерации пароля несколько раз и посмотреть как изменится счетчик.

"""


def create_counter():
    counter = 0
    print(counter)

    def generate_pasword():
        nonlocal counter
        sum_string = 'abcdefghijklmnopqrstuvwxyz'
        paassword = ""
        for letter in range(int(len(sum_string) / 8)):
            paassword += sum_string[letter]
        print(paassword)
        print(counter, " counter")
        counter += 1

    return generate_pasword


passt = create_counter()
passt()
passt()
passt()

print("this my av")


def make_averager():
    last_sum = 0
    index_element = 0

    def averager(new_value):
        nonlocal last_sum
        nonlocal index_element
        last_sum += new_value
        index_element += 1
        return last_sum / index_element

    return averager


avg = make_averager()
print(avg(11))
print(avg(12))

"""
С помощью функции map преобразовать случайного список целых чисел 
в новый список где каждый елеменет будет умножен на 2
"""


def mult_by_tow(list_random):  # function to multiply by 2
    return list_random * 2


list_rand = random.sample(range(1, 10), 5)
print(list_rand)
list_multipl_by_2 = list(map(mult_by_tow, list_rand))
print(list_multipl_by_2)

"""
С помощью функции filter выбрать только положительные целочисленные елементы случайного списка

"""


def umn2(list_random):
    return list_random > 0 and list_random % 1 == 0


list_rand_simple = random.sample(range(-20, 20), 6)
print(list_rand_simple)
list_filter = list(filter(umn2, list_rand_simple))
print(list_filter)


# С помощью функции reduce умножить все числа в списке

def func_red(sum1, sum2):
    return sum1 * sum2


list_reduce = random.sample(range(1, 20), 3)
print(list_reduce)
lis_red = reduce(func_red, list_reduce)
print(lis_red)


list_string = ['1', '2', '3', '4', '5']
print(list_string)
list_int = list(map(int, list_string))
print(list_int)


# С помощью функции map преобразовать список с милями в список с километрами, где 1 mile = 1.6 km
def mile_to_km(sum_list):
    return round((sum_list*1.6), 3)


list_mile = list(map(mile_to_km, list_int))
print(list_mile)