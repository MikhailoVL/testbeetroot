import random
import sys

print("Task 1 Написать функцию, которая будет принимать температуру по цельсию и возвращать ее перевод в температуру по фаренгейту по формуле: (temp - 32) * (5/9)")

temper = 20

def temperatur(celsiy):
    print(celsiy * (5/9)+32)

temperatur(temper)

print("Task 2 Написать функцию поиска минимума в произвольном количестве элементов переданных в функцию")

list_2_1 = list(random.sample(range(1, 101), 10))

def minimum(list_2):
    mini = list_2[0]
    for i in list_2:
        if mini > i:
            mini = i
    return mini
print(list_2_1)
print(minimum(list_2_1))

print("Task 3 Написать функцию которая принимает два аргумента: первый аргумент отвечает за выбор пользователя: минимум или максимум, второй аргумент - список элементов в котором нужно найти минимум или максимум")

user_input = input("Enter choice min or max :")
list_3 = list(random.sample(range(1,101),10))
print(list_3)


def min_f(sum_list):
    minimal_maximum = sum_list[0]
    for element in sum_list:
        if minimal_maximum > element:
            minimal_maximum = element
    return minimal_maximum

def max_f(sum_list):
    minimal_maximum = sum_list[0]
    for element in sum_list:
        if minimal_maximum < element:
            minimal_maximum = element
    return minimal_maximum

actions = {
    "min" : min_f,
    "max" : max_f
    }

def my_min_max(dict_3, user_in, list_sum):
    print(dict_3[user_in](list_sum))
        
my_min_max(actions, user_input, list_3)

print("Task 4 Написать функцию пересечения и функцию объединения неограниченного количества последовательностей")

list_4_1 = list(random.sample(range(1,10),3))
list_4_2 = list(random.sample(range(1,10),3))
print(list_4_1, list_4_2)

def unification(*args):
    sum_list = []
    for item in args:
        sum_list.extend(item)
    return sum_list

print(unification(list_4_1, list_4_2))


def intersectio(*args):  
    sum_set = set()
    for element in args:
        if len(sum_set) == 0:
            sum_set = set(element)
        else:
            sum_set = sum_set.intersection(set(element))
    return sum_set
    
print(intersectio(list_4_1, list_4_2))

print("Task 5 Имитировать работу функции print(*args, sep=’’, end=’\n’) используя поток вывода sys.stdout.write(text)")
my_str = "Привет мир"
my_str_2 = " я тут"
def my_print(*args, sep =" ", end= "\n"):
    new_str = sep.join(args)
    sys.stdout.write(new_str + end)
        
my_print(my_str, my_str_2, sep="!")
    

print( "Task 6 Написать функцию, которая принимает строку как аргумент и возвращает ее в обратном порядке не используя функцию reversed или срезы.")

my_str_rev = "hellow world"
def revers_str(sum_str):
    for item in sum_str[::-1]:
        print(item)

revers_str(my_str_rev)

print("Task 7 Написать функцию для подсчета периметра фигуры в зависимости от того какую фигуру укажет пользователь")

def kv_perimetr():
    a = int(input("введите длинну одной стороны квадрата"))*4
    return a

def treang_perimetr():
    a, b, c = input("введите 3 стороны треугольника через пробел").split()
    return int(a) + int(b) + int(c)

def circle_perimetr():
    radius = int(input("Enter radius you circle"))
    return 2*3.1415*radius

figur = {
    "квадрат" :kv_perimetr,
    "треугольник" : treang_perimetr,
    "круг" : circle_perimetr
    }

user_figa = input("Переиметр какой фигуры вам нужно подсчитать? квадрат, треугольник, круг")
print (figur[user_figa]())

print("Task 8 Написать функцию, которая генерирует матрицу размером n*n с рандомными числами. Размер указывает пользователь")
ma_size = int(input("enter size matrix :"))

def matrixs(matrix_size):
    list_matrix = [[random.randint(1,10) for y in range(matrix_size)] for x in range(matrix_size)]


    for item_i in range(matrix_size):
        for item_j in range(matrix_size):
            if list_matrix[item_i][item_j] < 10:
                print("0" + str(list_matrix[item_i][item_j]), end= " ")    
            else:
                print(list_matrix[item_i][item_j], end= " ")
        print("") 
    return list_matrix
matrixs(ma_size)

print("Task 9 Используя матрицу из прошлого примера, написать функцию, которая вернет номер ряда с максимальной суммой элементов.")

def count_row_matrix(matrix_for_count):
    row = 1
    count_row = sum(matrix_for_count[0])
    for item_i in range(len(matrix_for_count)):
        if count_row < sum(matrix_for_count[item_i]):
            count_row = sum(matrix_for_count[item_i])
            row = item_i + 1
    return row
 

print(count_row_matrix(matrixs(ma_size)))
            
    
    
    
    
    
    
    






















