import random

print("Task 1 Посчитать количество 9 в списке.")
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nine = 0 
print("index in loop for")
for item in list_1:
    if item == 9:
        nine += 1
        print("nine in list : " + str(nine))
        
    

print("index in item loop while")

i = 0
nine = 0
while i < len(list_1):
    if list_1[i] == 9:
        nine += 1
        print("nine in list : " + str(nine))  
    i += 1 

print("Task 2 Вывести количество четный и нечетных елементов в рандомной последовательности.")

list_2 = random.sample(range(10),10)
print("My list, task 2 : " + str(list_2))

print("my  even number loop \"for\"")
for item in list_2:
    if item % 2 == 0:
        print(item)

print("my  even number loop \"while\"")
i = 0
while i < len(list_2):
    if list_2[i] % 2 == 0:
        print(list_2[i])
    i += 1

print("""Task 3 Пользователь должен ввести последовательность чисел через пробел.Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.""")

list_3 = list(input("введите последовательность чисел через пробел").split())

print("print my list task loop for : " + str(list_3))

i = 0
a = set()
for item in list_3:
    if item not in a:
        print( "No")
        a.add(item)
    else:
        print("Yes")
print("print my list task loop while : " + str(list_3))


a =set()
while i < len(list_3):
    if list_3[i] not in a:
        print( "No")
        a.add(list_3[i])
    else:
        print("Yes")
    i += 1 

print("""Task 4 Написать функцию, которая будет принимать пароль. Если в пароле есть 1 большая буква и хотя бы 5 цифр, и его длина не менее 10 символов вывести: “Your password is strong.” в противном случае “Your password is not strong enough.""")

pasword ="12345Asdfg"
didg = 0
mega_alfa = False

if len(pasword) >=10:
    for item in pasword:
        if not item.isalpha():
            didg += 1
        if item.isupper():
            mega_alfa = True
    if didg == 5 and mega_alfa:
        print("-Your password is strong.")
else:
    print("-Your password is not strong enough.")


print("Task 5 Посчитать факториал для введенного пользователем числа")
integer_user = int(input(" введите число :"))
pc_int=1
print(range(integer_user + 1))
for item in range(integer_user + 1):
    print(item)
    if item > 0:
        pc_int *= item
print(f"факториал от числа {integer_user}  = {pc_int}")

print ("""Task 6 С помощью random сгенерировать 2 целых числа и спросить у пользователя ответ суммы этих чисел. Если пользователь посчитал верно то засчитать ему одно очко. Повторять пока пользователь не введет ‘q’.""")
result_user = 0
while True:
    f_random_int_task_6 = random.randint(1,100)
    s_random_int_task_6 = random.randint(1,100)
    print(f"Напишите сумму двух чисел : {f_random_int_task_6} + {s_random_int_task_6}")
    input_6 = input("Enter result or \'q\' for exit :")
    if input_6 == "q":
        break
    elif int(input_6) == (f_random_int_task_6 + s_random_int_task_6):
        result_user += 1
        print(f"your result : {result_user}")
    else:
        print("your enter not correct, try again")


print("""Task 7  Вывести последовательность Коллатца для числа введенного пользователем. Остановится когда число достигнет 1""")
user_input_7 = int(input('Enter: '))

list_kolatza = [user_input_7]
i = 0

while list_kolatza[i] != 1:
    if list_kolatza[i] % 2 == 0:
        list_kolatza.append(list_kolatza[i] // 2)
    else:
        list_kolatza.append(list_kolatza[i] * 3 + 1)
    i += 1
print(list_kolatza)

print(" Task 8 Вывести последовательность Фибоначчи где количество элементов последовательности задается пользователем")

user_input_iteration = int(input("Enter count fibonacci"))
list_fibonacci = []
for i in range(user_input_iteration):
   # print(str(i) + "my count")
    if i >4 :
        list_fibonacci.append(list_fibonacci[i-1]+list_fibonacci[i-2])
    elif i > 1 and i <=4:
        list_fibonacci.append(i-1)
    else:
        list_fibonacci.append(i)
print(list_fibonacci)

print(""" Task 9 Дано нечетное число n. Создайте вложеный список из n×n элементов, заполнив его символами \".\"(каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. В результате должны образовывать изображение снежинки. Выведите полученный массив на экран, разделяя элементы массива пробелами.""")
n = 9
d = [["." for j in range(n)] for i in range(n)]

for column in range(n):
    for row in range(n):
        if column == n // 2 or column==row or (row ==n//2) or row == n - column -1:
            d[column][row] = "*"
    

for item_i in range(n):
    for item_j in range(n):
        print(d[item_i][item_j], end= " ")    
    print("")



