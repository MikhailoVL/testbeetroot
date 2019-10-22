import os.path
import random
import json
print("Task 1 Создать файл nums.txt с рандомными цифрами и нужно среди них найти самую большую цифру и написать его уже в новый max_num.txt файл")

print(os.path.dirname(__file__))

my_python_f_1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), "nums.txt")

my_python_f_1_1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), "max_num.txt")

list_9_1 = random.sample(range(1,20),10)
my_str=" ".join(map(str,list_9_1))

with open(my_python_f_1, "wr+") as my_file:
    my_file.write(my_str)
    new_str = max(map(int,my_file.read().split()))
my_file.close()

with open(my_python_f_1_1, "w") as my_file_2:
    my_file_2.write(str(new_str))
my_file_2.close()

print("Task 2 Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел. Напишите программу, которая подсчитывает и выводит на экран общую сумму чисел, хранящихся в этом файле.")

my_python_f_2 = os.path.join(os.path.dirname(__file__),"nums1.txt")

list_9_2 = random.sample(range(1, 100), 10)
my_str = " ".join(map(str,list_9_2))
my_str_for_read = "" 
print(my_str)

with open(my_python_f_2, "w+") as f_sum:
    f_sum.write(my_str)
    f_sum.seek(0,0)
    my_str_for_read = sum((int(x) for x in f_sum.read().split()))
  
print(my_str_for_read)

print("Task 3 Посчитать количество строк в файле и количество слов и символов в каждой строке")

string_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eros elit, mollis vel mi tempor, imperdiet tincidunt risus. Vivamus euismod, arcu eu fringilla malesuada, lacus metus placerat justo, ut ultrices mi nulla et dolor. Suspendisse mollis leo at pretium pellentesque. Suspendisse nunc purus, consectetur in tincidunt ut, mattis eu leo. Vestibulum malesuada nec quam ut bibendum. Donec ornare ex eget ornare iaculis. Fusce ac lacus in quam faucibus gravida. Etiam hendrerit, sem sed bibendum aliquet, felis purus accumsan nibh, ut interdum augue ante vel nisi. Pellentesque ac purus ultricies, aliquam est nec, rutrum libero. Quisque auctor orci sapien, sit amet porttitor nulla volutpat quis. Aenean mi leo, viverra nec ante in, imperdiet fermentum diam. Sed justo velit, auctor eu libero sed, tincidunt consequat enim. Fusce ut molestie augue. Proin a tristique nisl.

Nullam mattis elementum massa id varius. Sed sodales neque id diam sodales mattis mattis ac purus. Phasellus vitae eros cursus, interdum justo eget, mollis erat. Sed tellus turpis, pharetra eu malesuada et, pulvinar a metus. Mauris dignissim porta commodo. Praesent vitae lorem risus. Donec congue ex a risus maximus, vel auctor ex luctus. Praesent blandit elit est, et fermentum velit aliquet ac. Cras sed magna eu orci ullamcorper mollis. Donec tincidunt libero quis diam convallis, et sagittis risus suscipit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Fusce tempor, nibh vel fermentum varius, mi urna blandit elit, in cursus lorem urna at dui. Vivamus pretium nunc mi, non sollicitudin eros pharetra et. Morbi finibus sapien vel neque blandit semper. Nullam eros sapien, pretium sed volutpat non, facilisis sit amet orci.

Curabitur vitae varius nisi, quis consequat velit. Morbi in neque posuere, dignissim quam quis, mollis orci. Etiam vestibulum massa a eros blandit, vel volutpat velit elementum. Nulla sed nibh vitae metus pharetra consequat nec viverra odio. Suspendisse sapien tortor, dapibus non turpis vel, volutpat mollis diam. In vel metus ipsum. Ut blandit sapien quis leo pharetra placerat. Fusce ac lectus a elit fermentum fringilla vitae nec arcu. Mauris gravida, velit quis malesuada fermentum, nisi neque luctus libero, ut aliquam mauris est vel orci. Vivamus rhoncus velit vitae convallis auctor. Quisque ultricies fringilla varius. Etiam et sollicitudin orci, at interdum odio. Nulla facilisi.

Integer posuere leo lacus, et maximus elit imperdiet id. Sed efficitur facilisis odio, a pharetra turpis ullamcorper vel. Sed commodo leo vitae ex euismod molestie. Nulla arcu tortor, egestas at egestas sed, tempor eget tortor. Fusce et porta nisi, nec fermentum ante. Maecenas ante justo, feugiat vitae est at, dignissim convallis purus. Curabitur et eleifend nisi. Morbi sagittis nulla mi, vel placerat metus euismod vitae. Morbi volutpat turpis sed nibh dictum interdum. Nullam cursus quis sem ut aliquet. In vitae mollis purus. Quisque placerat sollicitudin ipsum sit amet egestas.

Cras pulvinar metus nec eros dignissim, at tincidunt erat fringilla. Ut non turpis scelerisque, posuere neque eu, interdum nisl. In tincidunt erat at commodo pharetra. Proin iaculis molestie lectus, quis semper nisi eleifend sed. Aenean a metus ac ex tempor molestie. Quisque ligula elit, consectetur sit amet tempus id, pellentesque eu dui. Nulla facilisi. Nunc laoreet magna nulla, at rutrum neque accumsan posuere. Nunc porta enim quam, eu convallis mauris tempus ut."""

my_path = os.path.join(os.path.dirname(__file__), "task_3.txt")
count_words = 0
count_char = 0
count_line = 0
with open(my_path , "w+") as big:
    big.write(string_text)
    big.seek(0, 0)
    count = big.read().split()
    big.seek(0, 0)
    count_char = list(big.read())
    big.seek(0, 0)
    for line in big:
        if line != "\n":
            count_line += 1
print(len(count_char), ": char")
print(len(count), " : word")
print(count_line, ": line")

print("Task 4 Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит пустая строка.")

my_path_4 = os.path.join(os.path.dirname(__file__), "task_4.txt")
    
with open(my_path_4, "w+") as file_4:
    user_input = input("Enter sum string :")
    while user_input:
        file_4.write(user_input + '\n')
        user_input = input("Enter sum string :")

print("Task 5 В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу. Создать отдельные файлы по классам.")
    

my_path_5 = os.path.join(os.path.dirname(__file__), "task_5.txt")
dict_class_1b = {
    "Петров Иван Иванович" : 4,
    "Генадиев Генри Михалыч" : 2,
    "Змеев Герзун Эдмундович" : 1,
    "Пакемон Орион Петрович" : 5,
    "Перун Петр Павлович" : 3,
    "Кергизюм Генадий Федорович" : 4,
    "Никрасов Василий Петрович" : 5    
    }
count_student = len(dict_class_1b)
all_mark = 0

with open(my_path_5, "w+") as file_5:
    for student, mark in dict_class_1b.items():
        file_5.write(str(student)+ " : "+ str(mark) + "\n")
        if mark < 3:
            print(student, " : ", mark)
        all_mark += mark
print("средний бал по классу : ", round((all_mark/count_student),2))


print("Task 6 Прочитать файл https://jsonplaceholder.typicode.com/todos, записать в новый файл все объекты с completed: true")

my_file_6_1 = "/home/miha/Рабочий стол/wer/task_6.json" 
my_file_6_2 = "/home/miha/Рабочий стол/wer/task_6_1.txt"
dict_6 = {}
with open(my_file_6_1, "r") as big_file:
    dict_6 = json.load(big_file)

with open(my_file_6_2, "w+") as small_file:
    for key in dict_6:
        
        for x, value in key.items():
            print (x, value)
            if x == "completed" and value:
                small_file.write(str(key) +"\n")

print("Task 7  Посчитать количество повторяющихся слов в первом абзаце https://ru.lipsum.com/feed/html из файла.")

my_file_7 = "/home/miha/Рабочий стол/wer/text_7.txt" 

first_line = ""

with open(my_file_7, "r") as file_7:
    first_line = file_7.readline().split()


dict_item = {}
for word in first_line:
    if word in dict_item:
        dict_item[word] += 1
    else:
         dict_item[word] = 1

for keys in dict_item.items():
    print(keys)

print("Task 8 Создать два файла .json из https://jsonplaceholder.typicode.com/todos в одном файле содержится id и title, в другом файле - id и completed. В результирующий файл записать JSON: {\"id\": 56, \"title\": \"\", \"completed\": true}\")")


my_file_8_1 = "/home/miha/Рабочий стол/wer/seven_1.json" 
my_file_8_2 = "/home/miha/Рабочий стол/wer/seven_2.json" 
my_file_8_3 = "/home/miha/Рабочий стол/wer/seven_3.json" 
my_file_8_4 = "/home/miha/Рабочий стол/wer/seven_4.json" 
dict_8 = {}
dict_8_2 = {}
dict_result = []

def id_title(dct):
    dct_8_2 = {}
    for key, value in dct:
        if key == "id":
            dct_8_2[key] = value
        if key == "title":
            dct_8_2[key] = value
    return dct_8_2
    
    
def id_completed(dct):
    dct_8_2 = {}
    for key, value in dct:
        if key == "id":
            dct_8_2[key] = value
        if key == "completed":
            dct_8_2[key] = value
    return dct_8_2
    
def resultetion(dct):
    dct_8_2 = {}
    for key, value in dct:
        if key == "completed":
            dct_8_2[key] = value
    return dct_8_2

with open(my_file_8_3, "r+") as seven_3:
    #read from fail
    dict_8 = json.load(seven_3, object_pairs_hook = id_title)
    seven_3.seek(0, 0)
    dict_8_2 = json.load(seven_3, object_pairs_hook = id_completed)  
    #writ in json fail
    with open(my_file_8_1, "w+") as seven_3_1:
        json.dump(dict_8, seven_3_1, indent = 1)
    #writ in json fail
    with open(my_file_8_2, "w+") as seven_3_2:
        json.dump(dict_8_2, seven_3_2, indent = 1)

#write int to result fail
with open(my_file_8_4, "w+") as result:
    with open(my_file_8_1, "r") as seven_3_1:
        dict_8 = json.load(seven_3_1, object_pairs_hook = id_title)
    with open(my_file_8_2, "r") as seven_3_2:
        dict_8_2 = json.load(seven_3_2, object_pairs_hook = id_completed)
#    dict_result = (di for i in range(len(dict_8)) for y in range(len(dict_8_2))
    for elem in range(len(dict_8)):        
       dict_8[elem].update(dict_8_2[elem])
       dict_result.append(dict_8[elem])
    #print(dict_result)
    json.dump(dict_result, result, indent = 1)












