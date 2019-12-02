import random
import os

sum_list = random.sample(range(1, 20), 10)
print(sum_list)


def sum_l(sum_l_):
    if len(sum_l_) == 1:
        return sum_l_[0]
    return sum_l(sum_l_[:-1]) + sum_l_[-1]


print(sum_l(sum_list))

polindrom = "madam"
length = len(polindrom)


def rec_polindrom(s_string):
    if len(s_string) == 1 or not s_string:
        return True
    if s_string[0] != s_string[-1]:
        return False
    else:
        return rec_polindrom(s_string[1:-1])


print(rec_polindrom(polindrom))

str_eng = "example"

#индусский код
def rec_str(eng_str):
    if len(eng_str) % 2 == 0:
        if len(eng_str) == 2:
            return "(" + eng_str + ")"
        else:
            return "(" + eng_str[0] + rec_str(eng_str[1:-1]) + eng_str[-1] + ")"
    else:
        if len(eng_str) == 1:
            return "(" + eng_str + ")"
        else:
            if len(eng_str) > 0:
                return "(" + eng_str[0] + rec_str(eng_str[1:-1]) + eng_str[-1] + ")"


#
# def rec_str(eng_str):
#     if len(eng_str) <= 2:
#         return "(" + eng_str + ")"
#     return "(" + eng_str[0] + rec_str(eng_str[1:-1]) + eng_str[-1] + ")"


print(rec_str(str_eng))
print(rec_str("exammmple"))
print(rec_str("exammple"))
print(rec_str("card"))


def fun_stepen(integer, step):
    if step == 1:
        return integer
    return fun_stepen(integer, step - 1) * integer


print(fun_stepen(8, 4))


def rec_print_direct_in_feil(path_dir):
    for file_dir in os.listdir(path_dir):
        if os.path.isdir(os.path.join(path_dir, file_dir)):
            print(os.path.join(path_dir, file_dir))
            rec_print_direct_in_feil(os.path.join(path_dir, file_dir))
        else:
            print("\t " + file_dir)


my_path = os.path.dirname(os.path.dirname(__file__))

print("111111" + my_path)


rec_print_direct_in_feil(my_path)