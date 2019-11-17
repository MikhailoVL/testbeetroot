import random


print("Task 1 Подсчитать количество каждого элемента в списке. Результат в виде словаря")
list_1 = [1, 2, 1, 2, 3, 4]
dict_1 = {}

for item in list_1:
    if item in dict_1:
        dict_1[item] += 1
    else:
        dict_1[item] = 1
print(dict_1)

print("Task 2 Вывести количество четный и нечетных елементов в рандомной последовательности.Результат в виде словаря")

list_2_my_randoms = random.sample(range(1, 101), 10)
dict_2= {"even" : 0, "not_even" : 0}
print(list_2_my_randoms)
for item in list_2_my_randoms:
    if item % 2 == 0 :
        dict_2["even"] += 1
    else:
        dict_2["not_even"] += 1
print(dict_2)

print("Task 3 Для каждого слова из данного текста https://ru.lipsum.com/feed/html подсчитайте, сколько раз оно встречалось в этом тексте ранее. Результат в виде словаря")

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis tincidunt leo in lacus volutpat pharetra. Vivamus a risus justo. Aenean ultricies at felis at feugiat. Duis leo tellus, lacinia ac magna ut, viverra laoreet erat. Fusce porta vulputate ullamcorper. Vivamus metus tortor, malesuada at ullamcorper eu, consectetur at urna. Morbi non eros velit. Suspendisse sit amet tellus efficitur, porttitor massa sed, sagittis odio. Cras ante augue, efficitur luctus ligula facilisis, pulvinar pharetra sapien. Curabitur scelerisque tellus sit amet massa cursus imperdiet. Vivamus semper nibh sed fermentum consequat. Etiam mollis sapien at arcu pharetra cursus. Morbi tincidunt est quis arcu tempor cursus. Suspendisse et congue urna. Phasellus ut lectus odio. Quisque viverra dignissim erat, at finibus augue faucibus at.

Donec viverra semper rutrum. Phasellus id lacus erat. Aenean finibus leo nec sagittis lacinia. Curabitur varius dui id nisi ultricies interdum. Morbi condimentum felis urna, id pulvinar est scelerisque in. Nullam non dui ornare, laoreet ipsum vel, ullamcorper tortor. Vivamus pellentesque, massa nec tristique lobortis, leo dolor dignissim diam, molestie luctus velit elit eu sapien. Cras mollis magna nec libero vestibulum ornare. Duis rutrum, dui nec facilisis sagittis, tortor nulla maximus purus, id mollis nunc mauris ac ipsum. Etiam tincidunt tincidunt eros in ultrices. Praesent eu enim velit. Mauris pellentesque commodo ligula, a scelerisque libero congue ac. Curabitur tempus et urna sed posuere. Integer vehicula dapibus odio, at mollis odio fermentum quis.

Morbi gravida eget elit ac tincidunt. Cras iaculis lacinia felis, in semper augue. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse laoreet sit amet quam at mollis. Suspendisse quis urna sit amet est laoreet porttitor et ac justo. Pellentesque pellentesque mattis malesuada. In vulputate lobortis velit, vel ullamcorper tortor scelerisque aliquam. Proin finibus, mauris ut faucibus posuere, est urna vestibulum tellus, ut egestas nulla erat vel sem. Cras sagittis orci sed sapien sodales, a dictum sem ultrices. Curabitur efficitur mi quis orci fringilla, quis sodales tellus accumsan. Mauris pretium enim sed urna lobortis, id ornare lacus fringilla.

Nunc quis diam ligula. Donec in cursus ante, sed consequat odio. Phasellus dignissim convallis enim. Vivamus quis odio fermentum, eleifend erat ut, dignissim quam. Sed fringilla neque magna, et tempus augue viverra id. Sed finibus, enim quis semper sollicitudin, nibh nisi ultricies mauris, eu gravida urna sapien in odio. Etiam commodo ante non ipsum posuere rutrum. Aenean non nisl rhoncus nulla finibus viverra. Nullam vel massa nunc. Donec est risus, vulputate euismod cursus vitae, eleifend ut ex. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Integer vel ante nec lacus consectetur lacinia ut vel ante. Proin nec ornare arcu.

Nam cursus risus et ligula porta vehicula. Integer volutpat odio a purus imperdiet, ut malesuada elit convallis. Maecenas efficitur at mauris at suscipit. Integer vestibulum lacus lectus, aliquet vestibulum mi accumsan semper. Cras egestas bibendum fermentum. Phasellus eget suscipit nulla. Curabitur accumsan elit felis, in fringilla metus semper quis."""

list_3 = list(text.split())
dict_3 = {}

for item in list_3:
    if item in dict_3:
        dict_3[item] += 1
    else:
        dict_3[item] = 1

for key, value in dict_3.items():
    print(key, value)

print("Task 4 Вам дан словарь, состоящий из пар слов. {“Hello”: “Hi”, “Bye”: “Goodbye”, “List”: “Array”} Каждое слово является синонимом к парному ему слову. Все слова в словаре различны. Определить синоним для слова введенного пользователем.")

dict_4 = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}
user_input=input("Enter word \"Hello\" - \"Hi\", \"Bye\"-\"Goodbye\", \"List\"- \"Array\" ")


user_input = user_input.capitalize()
if user_input in dict_4 or user_input in dict_4.values():
    for key, value in dict_4.items():
        if user_input == key:
            print(user_input, " его синоним : " ,value)
        elif user_input == value:
            print(user_input, " его синоним : " ,key)
else:
    print("uncorrect enter")

print("Task 5 Пользователь вводит список чисел через пробел, вывести новый список в котором элементы из введенного пользователем списка будут умножены на 2 с помощью списковых включений.")
user_input_task_5 = input("Enter nomber vs space :").split()

user_input_task_5_1 = [int(x)*2 for x in user_input_task_5]

print(user_input_task_5_1)

print(" Task 6 Пользователь вводит список чисел через пробел, вывести новый список содержащий только четные элементы (с помощью списковых включений)")

user_input_task_6 = input("Enter nomber vs space :").split()

user_input_task_6_1 = [int(x) for x in user_input_task_6 if x % 2]

print(user_input_task_6_1)

print("Task 7 Дан список чисел от 1 до 31, обозначающий дни в месяце. Вывести список только рабочих дней месяца без выходных.(с помощью списковых включений)")

user_input_task_7 = list(range(1,31))
# x+1 == 6 + 1 -> число 7 у нас все время срабатывает, имитируем 7ку 
user_input_task_7_1 = [x for x in user_input_task_7 if x % 7 != 0 if (x+1) % 7 != 0  ]
print(user_input_task_7_1)

print("Task 8 Генерируется квадратная матрица (с помощью списковых включений). Найти сумма элементов ее главной и побочной диагоналей.")

len_matrix = int(input("len matrix :"))

list_matrix = [[random.randint(1,10) for y in range(len_matrix)] for x in range(len_matrix)]

diagonal_matrix = 0
side_diagonal_matrix = 0

for item_i in range(len_matrix):
    for item_j in range(len_matrix):
        if item_i == item_j :
             diagonal_matrix += list_matrix[item_i][item_j]
        if item_j == len_matrix - item_i - 1:
            side_diagonal_matrix += list_matrix[item_i][item_j]
            
print("diagonal_matrix :", diagonal_matrix, ", side_diagonal_matrix :",  side_diagonal_matrix)


for item_i in range(len_matrix):
    for item_j in range(len_matrix):
        if list_matrix[item_i][item_j] < 10:
            print("0" + str(list_matrix[item_i][item_j]), end= " ")    
        else:
            print(list_matrix[item_i][item_j], end= " ")
    print("")

print("Task 9 Попросить пользователя ввести информацию про членов его семьи записывая их имя и возраст в отдельные словари списка. Вывести имя самого пожилого человека в семье.")

famely_list = {}
famely = int(input("how many relative you have :"))
for name in range(famely):
    name_r = input("Enter name your relative : ")
    famely_list[name_r] = input("Enter age relative :")
    
print(famely_list)


print("Task 10 необходимо объединить два прайс-листа (задаются в виде словарей) с тем условием, что если наименование товара присутствует в обоих прайсах, то в итоговый прайс помещается тот, чья цена выше. (с помощью comprehensions)")

dict_10_1 = {"apple" : 10, "carrot" : 20, "peach" : 23, "banana" : 34}
dict_10_2 ={"pear" : 12, "plum" : 34, "cherry" : 22, "banana" : 34}
d = {}

for key, value in dict_10_1.items():
   value2 = dict_10_2.get(key)
    if value2 and value2 > value:
      d[key] = value2  


d = {key: value for key, value in dict_10_1.items if dict_10_2.get(key) and dict_10_2[key] < value}




    


























