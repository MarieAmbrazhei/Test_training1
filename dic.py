# import pprint
#
# school = {'1a': 10, '1b': 12, '1v': 15}
# print(school['1b'])
#
# school['1a'] = 14
# school['1b'] = 14
# school['1v'] = 14
#
# a = {'2b': 12}
# b = {'3c': 13}
# school.update(a)
# school.update(b)
# print(school)
# del school['1b']
# print(school)
#
#
# "'"
# Словари
# 1. Создайте словарь, связав его с переменной school, и наполните его данными, которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
# 2. Узнайте сколько человек в каком-нибудь классе.
# 3. Представьте, что в школе произошли изменения, внесите их в словарь:
# ◦ в трех классах изменилось количество учащихся;
# ◦ в школе появилось два новых класса;
# ◦ в школе расформировали один из классов.
# 4. Выведите содержимое словаря на экран
# "'"
# school = {
#     '1a' : 10,
#     '1b' : 12
# }
# pprint.pprint(school)
import collections

import passwords


# a, b = 1,2
# print(isinstance(a,int) and isinstance(b,int))
# print(a is not b and b is not a)
# print(a is b and b is a)
# print(isinstance(a,str) and isinstance(b,str))

# a, b = 1,2
# print(isinstance(a,str) or isinstance(b,int))
# print(a is  b or b is not a)
# print(a is b or b is a)
# print(isinstance(a,str) or isinstance(a,str))
# 4.

# a = 'T'
# if a:
#     print('True')
# else:
#     print("False")
# print(bool('qq') != False)

# a = [1, 5, 2, 9, 2, 9, 1]
# for item in a:
#     if a.count(item) == 1:
#         print(item)
# print(collections.Counter(a))
#
# 'A1213pokl' == ‘плохой
# пароль’
# 'bAse730onE' == ‘хороший
# пароль’
# 'asasasasasasasaas' == ‘плохой
# пароль’
# 'QWERTYqwerty' == ‘плохой
# пароль’
# '123456123456' == ‘плохой
# пароль’
# 'QwErTy911poqqqq' == ‘хороший
# пароль’

# passwords = ['A1213pokl', 'bAse730onE', 'asasasasasasasaas', 'QWERTYqwerty',
#              '123456123456', 'QwErTy911poqqqq ууу']
#
# for p in passwords:
#     if len(p) >= 10 and not p.isdigit() and not p.isalpha() and not p.isupper() and not p.islower() and p.isalnum():
#         print(f"{p}")
# a = 'ffgkrp dpoejv epofkpoe'
# b = a.split('')
# Напишите функцию calculate_average(numbers), которая принимает список чисел и возвращает их среднее арифметическое.
# def calculate_average(*numbers):
#     average_value = sum(numbers) / len(numbers)
#     return average_value
#
# #
# exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# filter_list(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]) => ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"] => ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
# ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"] => []
# filter_list = ["Mallard", "Hook Bill", "African", "Crested",
#                "Pilgrim", "Toulouse", "Blue Swedish", "Mallard",
#                "Hook Bill", "Crested", "Blue Swedish"
#                                        "Mallard", "Barbary", "Hook Bill",
#                "Blue Swedish", "Crested"
#                                "Mallard", "Barbary", "Hook Bill",
#                "Blue Swedish", "Crested"
#                                "African", "Roman Tufted", "Toulouse",
#                "Pilgrim", "Steinbacher"]
#
# exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim",
#            "Steinbacher"]
#
#
# def filter(filter_list, exclude):
#     for i in exclude:
#         if i in filter_list:
#             filter_list.remove(i)
#
#
# print(filter_list)
#
# filter(filter_list, exclude)
# "String" => "SSttrriinngg"
# "Hello World" => "HHeelllloo  WWoorrlldd"
# "1234!_ " => "11223344!!__  "

# string_given = "String"
# doubled_string = ''
# for item in string_given:
#     doubled_string += item*2
# print(doubled_string)

# doubled_string = "".join([letter * 2 for letter in string_given])
# print(doubled_string)
# Если х в квадрате больше 1000 - пишем "Hot" иначе - "Nope"

# list = ["50", 4, "12", 60]
# for i in list:
#     i = int(i)
#     if i ** 2 > 1000:
#         print(f"Hot: {i}")
#     else:
#         print(f"Nope: {i}")
# [] == 0
# [1, 2, 3] == 6
# [1.1, 2.2, 3.3] == 6.6x
# [4, 5, 6] == 15
# range(101) == 5050
# list_one = []
# list_two = [1, 2, 3]
# list_three = [1.1, 2.2, 3.3]
# list_four = [1, 2, 3]
# print(sum(list_two), "true" if list_two else 0)
# if sum(list_four):
#     print("OK")
# else:
#     print(0)

# value = range(101)
# value = list(value)956ik9
# if value:
#     print("true")
# else:
#     print(0)

# string_of_letters = "fizbbbuz"
# letter = "b"
# counter = 0
# for i in string_of_letters:
#     if i == letter:
#         counter += 1
# print(counter)
# print(string_of_letters.count("b"))
# 1)
# Проверка строки. В данной подстроке проверить все ли буквы в
# строчном регистре или нет и вернуть список не подходящих.
# dogcat => [True, []]
# doGCat => [False, ['G', 'C']]

# def find_uppercase_letters(given_string):
#     upper_letters = []
#     for letter in given_string:
#         if letter.isupper():
#             upper_letters.append(letter)
#     if upper_letters:
#         return [False, upper_letters]
#     else:
#         return [True, upper_letters]
#
#
# print(find_uppercase_letters(given_string='dogcat'))
# print(find_uppercase_letters(given_string='doGCat'))

# def numbers(x, t):
# #     result = x + t
# #     return result
#
# def function(some_args):
#     print(some_args)
#     print("asdfg")
#
# a = function(5)
# print(a)
#
# def summ(x, y):
#     return x + y
# a = summ(5,6)
# print(a)

# def func():
#     return 5
# print(func())
# def func(x):
#     print(x)
#     print("asdf")
#     return 3*x
# a = func(10)
# print(a)


# name1 = "Tom"
# height1 = 1.68
# weight1 = 52
#
# name2 = "kate"
# height2 = 1.70
# weight2 = 60
#
# name3 = "Bob"
# height3 = 2
# weight3 = 150
#
#
# def bmi_calculator(name, height, weight):
#     bmi = weight / (height ** 2)
#
#     print("Index is:" + str(bmi))
#
#     if bmi < 25:
#         return name + " не имеет лишнего веса"
#     else:
#         return name + " имеет лишний вес"
#
#
# bmi1 = bmi_calculator(name1, height1, weight1)
# bmi2 = bmi_calculator(name2, height2, weight2)
# bmi3 = bmi_calculator(name3, height3, weight3)
# print(bmi1)
# print(bmi2)
# # print(bmi3)
# given_string = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # for item in given_string:
# #     if item < 5:
# #         print(item)
# print([item for item in given_string if item < 5])
# def reverse_string(s):
#     return s[::-1]
#
# # Примеры использования
# print(reverse_string("hello"))  # "olleh"
# print(reverse_string("Python"))  # "nohtyP"

# def find_lower(string):
#     lower_let = string.islower()
#
#     if lower_let:
#         return [True, []]
#     else:
#         return [False, ['G', 'C']]
# print(find_lower('dogcat'))
# print(find_lower('doGCat'))

# def power(base, num=2):
#     if not isinstance(base, int):
#         return 0
#     return base ** num
# print(power(2, 3))

# def hello():
#     return 'Hello world'
# print(hello())

# def calc(a, b, c):
#     return a + b + c
# print(calc(1, 2, 3))

# def greet(name: str) -> str:
#     return 'Hello, ' + name
# print(greet("Mary"))
# a = list(range(5))
# print(a)

# def is_palindrone(data):


# if data == data[::-1]:
#         return True
#     return False
#
# print(is_palindrone("hello"))
# print(is_palindrone("level"))


# assert is_palindrone("hello") == False, 'not palindrone'
# assert is_palindrone("level") == True, 'is palindrone'
# print(is_palindrone(data="level"))
# print(is_palindrone(data="hello"))
# Напишите программу. Есть 2 переменные salary и bonus.
# Salary - integer, bonus - boolean. Если bonus - true,
# salary должна быть умножена на 10. Если false - нет
# 10000, True == '$100000'
# 25000, True == '$250000'
# 10000, False == '$10000'
# 60000, False == '$60000'
# 2, True == '$20'
# 78, False == '$78'
# 67890, True == '$678900'

# def calc(salary: int, bonus: bool) -> str:
#     if bonus:
#         salary *= 10
#         return f"${salary}"
#     return f"${salary}"
#
#
# assert calc(10000, True) == '$100000'
# assert calc(25000, True) == '$250000'
# assert calc(10000, False) == '$10000'
# assert calc(2, True) == '$20'
# print(calc(10000, True))
# import random
# import string
#
#
# def play_bulls_and_cows():
#     """
#     Play game "Bulls and Cows"
#     """
#
#     digits = list(string.digits)
#     random.shuffle(digits)
#     random_number = ''.join(digits[:4])
#     attempt = 0
#     while True:
#         hidden_four_digit_num = input("ENTER A FOUR-DIGIT NUMBER: ")
#         attempt += 1
#         bulls = 0
#         cows = 0
#         for elements in range(4):
#             if random_number[elements] == hidden_four_digit_num[elements]:
#                 bulls += 1
#             elif hidden_four_digit_num[elements] in random_number:
#                 cows += 1
#         print(f"{hidden_four_digit_num} contain {bulls} bull and {cows} cows")
#         if bulls == 4:
#             print(f"You won in {attempt} steps")
#             break
#
# play_bulls_and_cows()my