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
        print("Your password is strong.")
else:
    print("Your password is not strong enough.")


print("Task 5 Посчитать факториал для введенного пользователем числа")
integer_user = int(input(" введите число :"))
pc_int=1
for item in range(integer_user):
    pc_int *= item
print(pc_int)








