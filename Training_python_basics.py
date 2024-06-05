# a = 1
# b = 2
# c = a
#
# a = b
# b = c
# print(a, b)
# a = 1
# b = 2
# c = a
#
# b = c
# a = b
# print(a, b)
#
# a, b, c = 1, 2, "mary"
# print("a:", a, "b:", b, "c:", c)
#
# a = b = 2
# print(a, b)
#
# MAX_LENGHT = 3
# for i in range(MAX_LENGHT):
#     print(MAX_LENGHT - i)
#
#     a = 3
#     print(type(a))

1.5 + 4  # Целочисленное сложение
# print(1.5 + 4)

2 ** 10  # 2 в степени 10
# print(2 ** 10)

# print(type(3.5))

# print(type(10e-5), 10e-5)

# a = 0.1
# print(a + a + a)

from decimal import Decimal

# a = Decimal("0.1")
# print(a + a + a + a + a + a + a + a + a + a)

# print(bool(0), 0)
# print(bool(1), 1)

5 == 6

# a = 1
# print(a)
# if a == 1:
#     print("1")
# else:
#     print("2")

# message = ("123")
# print(type(message))

# message = int("123")
# print(type(message))

# MAX_LENGTH = 25
# for i in range(MAX_LENGTH):
#     print(MAX_LENGTH - i)
#
# a = None
# print(type(a))
# S1 = 'first'
# S2 = "second"
# print(S2, S1, sep="---")
# print(S1 + " " + S2)
#
# print('meow ' * 3)
# print(len('soul '))
# s = "soul"
# print(s[0])
# print(s[2])
#
# s = 'texttexttext'
# print(s[-2])
# s = 'te'
# print(s[-2])
# s = 'abcderwz'
# print(s[3:5])
# print(s[2:-2])
# print(s[:6])
# print(s[2:])
# print(s[::-1])
# print(s[:])
# print(s[::2])
# print(s[::3])
# print(s[::-1])
# print([1, 2, 3])
# print({"one": 1})
# print(3e5)
# a = "Mary"
# b = 32
# print("Name is {name}, age is {age}".format(name=a, age=b))
# print("Name is {0}, age is {1}".format(a, b))
# print("Name is {}, age is {}".format(a, b))
# name = "Bob"
# age = 25
# print(f"Name is {name}, age is {age}")

"""
**Типы данных**
    Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
    Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза, результат свяжите с переменной big_int.
    Измените значение, хранимое в переменной var_float, уменьшив его на единицу, результат свяжите с той же переменной.
    Разделите var_int на var_float, а затем big_int на var_float. Результат данных выражений не привязывайте ни к каким переменным.
    Измените значение переменной var_str на "NoNoYesYesYes". При формировании нового значения используйте операции конкатенации (+) и повторения строки (*).
    Выведите значения всех переменных.

**Строки**
    Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов. Извлеките из строки первый символ, затем последний, третий с начала и третий с конца. Измерьте длину вашей строки.
    Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы: первые восемь символов четыре символа из центра строки символы с индексами кратными трем переверните строку
    Есть строка: my name is {name}. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.
    Есть строка: test_tring = "Hello world!",

    Необходимо напечатать на каком месте находится буква wкол-во букв l
    Проверить начинается ли строка с подстроки: “Hello”
    Проверить заканчивается ли строка подстрокой: “qwe”
Siarhei — 05/06/2024 9:03 PM
round(<число>, 2)
"""

# msg = ("My name - is - Otti")
# akk = msg.split('-')
# print(akk)
# var_int = 10
# big_int = var_int * 3.5
# print(big_int)
# var_float = 8.4
# var_float -= 1
# print(var_float)
# print(round(var_int / var_float, 2))
# print(round(big_int / var_float, 2)

# var_str = "Yes"
# var_str2 = "No"
# print(var_str * 2 + var_str2 * 2)
# print(var_str, var_str2)

# a = "12345678"
# print(a[0])
# print(a[-1])
# print(a[2])
# print(a[-3])
# print(len(a))
#
# a = "12345678"
# print(a[0], a[-1], a[2], a[-3], len(a))

# a = "123456789123456"
# print(a[:8])
# print(a[3:7])
# print(a[::3])
# print(a[::-1])
# print(len(a)//2)
# s = 'abcdeifghjklperty'
# print(s[3:5])
# a = "Выведите зна"
# c = len(a) // 2
# print(a[:9], a[c - 2: c + 2])
# name = 'Marie'
# print(f"my name is {name}")
#
# test_string = "Hello world!"
# print(test_string.count("w"))
# print(test_string.index("w"))
# print(test_string.startswith("Hello"))
# print(test_string.endswith("Hello"))

# msg = 'www.my_site.com#about'
# print(msg.replace('#', '/'))
# color = ["red", "blue", "green"]
# print(color)
# color[0] = "pink"
# print(color)
#
# arr = [0, 5, 10]
# arr2 = arr
#
# print("Equals:", arr == arr2)
# print("Same object:", arr is arr2)
#
# print([1, 2, 3] + [4, 5, 6])
# list1 = ['physics', 'Biology', 'chemistry', 'maths']
# list1.reverse()
# print ("list now : ", list1)
#
# array = [100, 300, 750, 430, 230, 555, 970]
#
# print("max()", max(array))
# print("min()", min(array))
# print("sum()", sum(array))
# array = [100, 300]
# array_copy = array[:]
# print("max()", max(array))
# print("min()", min(array))
# array.sort()
# print(sorted(array_copy))
# print("max()", max(array))
# print("min()", min(array))
# print("sum()", sum(array))
# l = [0, [0,1,2], 5]
# print(l)
# l[1][1] = 6
# print(l)

# user_list = [1, 2, 3]
# user_list1 = ["K", 5, "D"]
# print(user_list1[1])
# """
# 		    Измените во втором списке последний элемент. Выведите список на экран
# """
# user_list2 = ["K", 5, "D"]
# user_list2[2] = 90
# print(user_list2)
#
# # """
# #   Соедините оба списка в один, присвоив результат новой переменной. Выведите получившийся список на экран
# # """
# mix = user_list1 + user_list2
# mix = []
# mix.append(88)
# print(mix)
# mix.append("rr")
# print(mix)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# y = set(a)
# c = set(b)
# w = []
#
# for i in y:
#     if i in c:
#         w.append(i)
# print(w)
# c = list(set(a) & set(b)

# e = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
# print(type(set(e)))
# print(type(list(set(e))))

# dd = [5, 1, 2, 3, 0, 1, 5, 0, 2]
# qq = [10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
#
# ss = qq.index(0)
# print(ss)
# print(qq[0:ss])
# print(sum(qq[0:ss]))
# print(sum(qq[:qq.index(0)]))
# a = 2.23456
# print("{:.3f}".format(a))
# print("{:.2f}".format(a))
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 444))
# msg = "H, {}!".format("Mary")
# # print(msg.format(msg))
# a = "Mary"
# b = "Helen"
# print(f'My name is {0}, her name is {1}')
# a = "mary"
# b = 33
# print("My name is " + a + ". I am " + str(b) + " old.")
# a = 2.23456
# print(f"{a:.2f}")
# a = "mary is my name"
# print("Capitalization", a.capitalize())
# print("Title", a.title())
# print("Upper", a.upper())
# print("Lower", a.lower())
# msg = "This is me"
# arr = msg.split()
# print(arr)
# msg = "".join(arr)
# print(msg)
# a = "This is name"
# print(a.replace("This", "is"))
# a = ["1, 2, 3"]
# join is for list
# split is for str
# print(' '.join(a[0].split()))
# print(a[0].replace(", ", ""))
# a = ['Hello', 'world']
# result = ','.join(a)
# print(result)
# a = 'hi hi hi'
# b = a.split()
# print(b)
# a = ''.join(b)
# print(a)
# a = ["1 2 3"]
# print(''.join(a[0].split()))

# a = "h h h"
# b = a.split()
# print(b)
# a = ''.join(b)
# print(a)

# msg = ["go", "do"]
# ing_addition = "ing"
# for word in msg:
#     print(word + ing_addition)
# # Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
# str_to_update = 'www.my_site.com#about'
# print(str_to_update.replace('#', "/"))
# Напишите программу, которая добавляет ‘ing’ к словам
# given_words = "do", "go", "join"
# ing_addition = "ing"
# for word in given_words:
#     print(word + ing_addition)
# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
# name_to_update = 'Ivanou Ivan'
# print(' '.join(name_to_update.split()[::-1]))


# # Напишите программу которая удаляет пробел в начале, в конце строки
# words_with_spaces = ['    spaces_before_word', 'spaces_after_word    ']
# # for word in words_with_spaces:
# #     print(word.replace(' ', ''))
# #     print(word.strip())
# print([word.strip() for word in words_with_spaces])
#
# # Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
# # Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению.
# # "pARiS" >> "Paris"
# camel_case_names = ['pARiS', 'mOSCOw', 'pYthoNIsAwesOMe']
# print([word.title() for word in camel_case_names])

# a = "pAris"
# print("pAris", a.capitalize())
# text_alignment = "Python is awesome"
# NUM_CHR = 60
# print(text_alignment.center(NUM_CHR))
# print(text_alignment.ljust(NUM_CHR))
# print(text_alignment.rjust(NUM_CHR))

# true_or_false = "fkgkHHghrg"
# print(true_or_false.isdigit())
# print(true_or_false.isalpha())
# print(true_or_false.islower())
# start_and_end = "This is Python baby"
# print(start_and_end.startswith("This"))
# print(start_and_end.endswith("baby"))

# Методы lstrip(), rstrip() и strip() используются для удаления пробельных символов
# (или других указанных символов) с начала, конца
# или обоих концов строки соответственно.
# removing_whitespace_characters = ["   This python baby   "]
# print([word.strip() for word in removing_whitespace_characters])
# print([word.rstrip() for word in removing_whitespace_characters])
# print([word.lstrip() for word in removing_whitespace_characters])
# deld = ["this is Python, baby"]
# print([word.strip() for word in deld])
#
# test_string = "onetesttwothree"
#
# print(test_string.find("test"))
# print(test_string.index("s"))

# a, b = "go", "do"
# c = a + 'ing', b + 'ing'
# print(c)
# test_string = "onetesttwothree"
# print(test_string.find("test"))
# print(test_string.index("s"))
# color = ["red", "blue", "green"]
# print(color)
# a = "a b"
# # print(a.replace("a", "b"))
# test_string = "onetoone"
# print(test_string.strip("on"))
# test_string_two = " one"
# print(test_string_two.strip("o"))
# test_string = "onetwothree"
# print(test_string.find("f"))
# test_string_two = "onetwo"
# print(test_string_two.index("t"))
# a = list([1, 1, 1])
# b = a
# print("1:", a, a is b)
# a[1] = 2
# print(a)
# print(b)
# arr = [0, 5, 10]
# arr2 = list(arr)
# arr3 = arr2.copy()
#
# print("Equals:", arr == arr2 == arr3)
# print("Same object:", arr is arr2, arr2 is arr3)
# a = ['Hi!'] * 4
# print(a)
# array = ["apple", 10, 0.5, 3 + 7j, [5, 6, 7], {"a": "b"}]
# print("Длина:\t", len(array))
# print("Размер:\t", array.__sizeof__())
# array = ["apple", 10, 0.5, 10]
# print(10 in array)
# print(array.index(10))
# print(array.count(10))
#
# array.append("the end")
# print(array)
#
# array.insert(3, "center")
# print(array)
#
# array2 = ['New', 'list']
# array.extend(array2)
# print(array)
# array = [1, 2, 2, 3, 4, 5, 6, 7]
# slice = array[3:-1]
# slice[0] = "Hello"
# print(slice)
# # Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
# string = "Robin Singh"
# creating_list = string.split()
# print(creating_list)
#
# #"I love arrays they are my favorite" =>
# # ["I", "love", "arrays", "they", "are", "my", "favorite"]
# long_string = "I love arrays they are my favorite"
# creating_long_list = long_string.split()
# print(creating_long_list)
#
# # Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# first_list = ["Ivan", "Ivanou"]
# string_one = "Minsk"
# string_two = "Belarus"
# final_list = first_list + [string_one, string_two]
# print(final_list)

# fullname_in_list = ["Ivan", "Ivanou"]
# city_in_str = "Minsk"
# country_in_str = "Belarus"
# general_names_in_list = []
# general_names_in_list.extend(fullname_in_list + [city_in_str, country_in_str])
# print(general_names_in_list)

# Напечатайте текст: “Привет, Ivan Ivanou!
# Добро пожаловать в Minsk Belarus”
# fullname_in_list = ["Ivan", "Ivanou"]
# city_in_str = "Minsk"
# country_in_str = "Belarus"
# print("Привет,", ' '.join(fullname_in_list) + "!", "Добро пожаловать в", city_in_str, country_in_str)

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
# list_of_words = ["I", "love", "arrays", "they", "are", "my", "favorite"]
# str_of_words = ' '.join (list_of_words)
# print(str_of_words)
# # Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# # удалите элемент из списка под индексом 6
# list_of_ten_positions = ["one", 2, 0.5, {"a": "b"}, "python", [3,6], 3, "THE BEST", 8, 9, "5g"]
# print("Длина:", len(list_of_ten_positions))
# list_of_ten_positions.insert(3, "Awesome_python")
# print(list_of_ten_positions)
# del list_of_ten_positions[6]
# print(list_of_ten_positions)
# Выводит уникальные данные
# list1 = ['maths', 'maths', 'rus']
# # print("list now:", list(set(list1)))
# a = [10, 20, 30, 40]
# for i in [10, 20, 30, 40]:
#     print(i)
# a = [10, 20, 30, 40]
# for i in enumerate(a):
#     print(i)

# row = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# matrix = row * 2
# for row in matrix:
#     print(row)
# matrix[0][0] = 1

# for row in matrix:
#     print(row)

# l = [0, [0, 1, 2], 5]
# # print(l)
# l[1][1] = 6
# # print(l[1], [2])
# print(l)
# длина списка
# Мы снова обращаемся к элементу с индексом 1 списка l, который
# является вложенным списком [0, 1, [2, 3]]. Затем мы обращаемся к
# элементу с индексом 2 этого вложенного списка, который является
# списком [2, 3]. Далее, мы используем len() для определения длины
# этого вложенного списка, которая равна 2.

# l = [0, [0, 1, [2, 3]], 5]
# # print(len(l[1] [2]))
# l = [0, [0, 1, [2, 3]], 5]
# print(l)
# l[1][2][1] = 6
# # print(l)
# l = [0, [0, 1, [2, 3]], 5]
# print(l)
# l[1][2].append(4)
# print(l)
# l = [0, [0, 1, [2, 3]], 5]
# print(l)
# l[1][2].insert(3,  "5")
# print(l)

# import copy
#
# test_1 = [1, 2, 3, [1, 2, 3]]
#
# test_copy = copy.copy(test_1)
# test_copy[3].append(4)
# print(test_1)
# print(test_copy)

# test_copy[3].append(5)
# print(test_1)
# print(test_copy)

# import copy
#
# test_1 = [1, 2, 3, [1, 2, 3]]
#
# test_copy = copy.copy(test_1)
# # test_copy[3].insert(3, "4")
# # test_copy[0] = 4
# test_copy.insert(3,4)
# print(test_1)
# print(test_copy)
# a = 5 / 3
# print(type(a), a)
# from decimal import Decimal
# a = Decimal("0.1")
# print(a * 10)
# import decimal
# float_division=4/3
# decimal_devision=decimal.Decimal(4)/decimal.Decimal(3)
# print("Result for float division of 4 by 3:")
# print(float_division)
# print("Result for decimal division of 4 by 3:")
# print(decimal_devision)
# number_of_obj = 1
# print(bool(number_of_obj))
# print(type(number_of_obj))
# no_result = None
# print(type(no_result), no_result)
# #
# def find_element(my_list_param, target_param):
#     for element in my_list_param:
#         if element == target_param:
#             return element
#     return None
#
#
# my_list_var = [1, 2, 3, 4, 5, 6]
# target_var = 6
# result = find_element(my_list_param=my_list_var, target_param=target_var)
#
# if result is None:
#     print(f"Элемент {target_var} не найден в списке.")
# else:
#     print(f"Элемент {result} найден в списке.")

# def find_element(list_param, obj_param):
#     for element in list_param:
#         if element == obj_param:
#             return element
#     return None
#
# list_var = [1, 2]
# obj_var = 2
# result = find_element(list_param=list_var, obj_param=obj_var)
#
# if result is None:
#     print(result)
# else:
#     print(f'Объект {obj_var}  найден в списке')
# s = 'tefryui'
# print(s[0])
# print(s[2])
# print(s[-2])
# print(s[-4])
# s = 'abcdef'
# print(s[::2])
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(my_list[0:8:2])
# s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(s[::2])
# print(s[::3])
# print(s[::-1])
# print([1, 2, 3])
# print({"one": 1})
# print(3e5)
# d = dict([(1, 1), (2, 4)])
# print(d)
# fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
# dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
# fishdog = {**fish, **dog}
# print(fishdog)
# d = dict.fromkeys(['a', 'b'], 100)
# print(d)
# c = {i: i ** 2 for i in range(10)}
# # print(c)
# from collections import Counter
#
# c = Counter([1, 2, 3, 1, 2, 3, 6, 3, 1, 3, 2, 3, 1, 3, 5, 2, 1, 2])
#
# print(c)
# a = "Mary"
# b = 23
# print('May name is {name}, age is {age}'.format(name=a, age=b))
#
# a = "Mary"
# b = 23
# print('Her name is {}, her age is {}'.format(a,b))
#
# a = "M"
# b = 2
# print('This is {}, this is {}'.format(a, b))
# print('This {name}, this {age}'.format(name=a,age=b))
# a = "M"
# b = 1
# print(f'Name is {a}, age is {b}')
# msg = "This is a test message"
#
# arr = msg.split()
# print(arr)
#
# msg = " ".join(arr)
# print(msg)
# print("\t".isprintable())

# a = "V"
# b = 32
# print('This is {name}, this is {age}'.format(name=a, age=b))
#
# c = "n"
# d = 12
# print(f'This is {c}, is {d}')

# def find_element(my_list, target):
#     for element in my_list:
#         if element == target:
#             return element
#     return None
#
# # Example usage of the function
# my_list = [1, 2, 3, 4, 5]
# target = 6
# result = find_element(my_list, target)
#
# if result is None:
#     print(f"The element {target} was not found in the list.")
# else:
#     print(f"The element {result} was found in the list.")
# a = "wargjpregblk erngorwpjgj4"
# print(len(a))
# a = "mary is girl"
# text = a.index("is")
# print(text)
# a = "mary is girl"
# print(a.isdigit())
# a = "mary is girl"
# print(a.strip("l"))
# # test_string = "onetesttonn"
# # print(test_string.strip("on"))
# print("m" in a)
# array = [100, 300, 750, 430, 230, 555, 970]
#
# print("max", max(array))
# l = [0, [0,1,2], 5]
# print(l)
# l[1][1] = 6
# print(l)
# Из
# заданной
# строки
# получить
# нужную
# строку:
# "String" = > "SSttrriinngg"
# "Hello World" = > "HHeelllloo  WWoorrlldd"
# "1234!_ " = > "11223344!!__  "
#
# a = ""
# str = "String"
# for i in str:
#     a += i * 2
#     print(a)
# a = 1
# if a == 1:
#     print("True")
# else:
#     print("False")
# if not 0:
#     print('true')
# else:
#     print('false')

# x = 'killer rabbit'
# if x == 'roger':
#     print('how’s jessica?')
# elif x == 'bugs':
#     print('what’s updoc?')
# else:
#     print('Runaway! Run away!')
# choice = 'ham'
# print({'spam': 1,
#  'ham': 2,
#  'eggs': 3}[choice])
# a = '1'
# print({'1': 'Mary', '2': 'Lola'}[a])
# choice = 'ham'
# if choice == 'spam':
#  print(24)
# elif choice == 'beef':
#  print(1)
# elif choice == 'ham':
#  print(1.3)
# else:
#  print("BAD")

# branch = {'spam': 1, 'ham': 2}
# # print(branch.get('banana', 'Bad choice'))
# choice = 'ham'
# if choice in branch:
#     print(branch[choice])
# else:
# #     print("bad choice")
# x = 'SPAM'
# if 'rubbery' in 'shrubbery':
#     print(x * 8)
#     x += 2
#     if x.endswith("NI"):
#         x *= 2
# #     print(x)
# if  1:
#     print("True")
# else:
#     print("False")
# a = 't' if  'spam' else z
# print(a)
# a = ['g', 't']
# print(a[bool('')])
# var_name = 1000
# if var_name != 100: print(f'hello {var_name}')
# while
# i = 5
# while i > 0:
#     print(i)
#     i -= 1
# else:
#     i = 0
# print("End")
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# for i in range(0, 10):
#     print(i)
# else:
#     print("End")
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)
# branch = {"ham": 1, "bacon": 2}
# choice = "bacon"
# if choice in branch:
#     print(branch[choice])
# else:
#     print("Bad choice")
# Правильно оформленная версия этого фрагмента приводится ниже – даже в
# таком простом примере, как этот, правильное оформление отступов д
# x = 'SPAM'
# if "rubbery" in "shrubbery":
#     print(x * 8)
#     x += "NI"
#     if x.endswith("NI"):
#         x *= 2
#         print(x)
# text  = "hello, mary"
# if "mary" in text:
#     text += " P"
#     print(text)
#
# x = 'SPAM'
# if "not_here" in "shrubbery":
#     print(x * 8)
#     x += "NI"
#     if x.endswith("NI"):
#         x *= 2
#     print
# X = [1]
#
# # if X:
# #     print("Z")
# # else:
# #     print("W")
# print("Z") if X else print("W")
# a = 'ham'
# print({'ham': 1,
#   'ban': 2}[a])
#
# branch = {'ham': 1, 'egg': 3}
# choice = 'ham'
# print({'spam': 1,
#  'ham': 2,
#  'eggs': 3}[choice])
# if choice == 'ham':
#     print("Right choice")
# elif choice == 'spam':
#     print('Bad choice')
# else:
#     print("the worst choice")
# print(choice.get('ham', 'bad choice'))
# if choice in branch:
#     print(branch[choice])
# else:
#     print("bad choice")
# a = {}
# a = 't' if {} else 'f'
# print((0 and 'f') or 'z')
# print(a)
# a = ["w", "e"][bool('')]
# print(a)
# x = 'spam'
# while x:
#     print(x, end=' ')
#     x = x[1:]
# Loop While
# a = 0
# b = 11
# while a < b:
#     print(a, end=" ")
#     a += 1
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)
# x = 10
# # while x:
#     x = (x -1)  # Или, x -= 1
#     if x % 2 != 0: continue  # Нечетное? – пропустить вывод
#     print(x, end=' ')
# while x:
#     x = x - 1
#     if x % 2 == 0:
#
# 1.
# def greet():
#     return 'Hello'
#
#
# print(greet())
# # 2
# def calc (a,b,c):
#     return a + b + c
# print(calc(1, 2, 3))
# #
# txt = ",,,,,rrttgg.....banana....rrr"
#
# x = txt.strip(",.grt")
# #
# # print(x)
# #
# txt = "banana     "
#
# x = txt.strip()
#
# print("de fe3", x, "-")

# print(tuple(map(int, ['1', ' 2', '3'])))
#
# list_1 = ['1', '2', '3']
# list_2 = []
# for i in list_1:
#     list_2.append(int(i))
#
# print(list_2)
# def bold_reg(reg):
#     print(1)
#     def wrapper(text1: str):
#         a = f'<b>{text1}</b>'
#         reg(a)
#
#     return wrapper


# def ita_reg(reg):
#     print(2)
#     def wrapper(text1: str):
#         a = f'<i>{text1}</i>'
#         reg(a)
#
#     return wrapper
#
#
# def under_reg(reg):
#     print(3)
#     def wrapper(text1: str):
#         a = f'<u>{text1}</u>'
#         reg(a)
#
#     return wrapper


# @bold_reg
# @ita_reg
# @under_reg
# def reg(text):
#     print(text)
#
#
# reg("hello")
# def duplicate(elememt: str, count: int) -> int:
#     return count * elememt
# print(duplicate.__annotations__
# Training
# a = 34
# b = 38
# # if a > b:
# #     print(f'{a} is greater than {b}')
# # elif a == b:
# #     print(f'{a} is equal to {b}')
# # else:
# #     print(f'{a} is less than {b}')
#
# # print(f'{a} is greater than {b}') if a > b else print(f'{a} is less than {b}')
# print(f'{a} is greater than {b}') if a > b else print(
#     f'{a} is equal to {b}') if a == b else print(f'{a} is less than {b}')

# a = 30
# b = 29
# c = 29
# if a > b or c > a:
#     print('Both conditions are True')
# else:
#     print('Bad condition')

# a = 1
# b = 3
# print('1') if a == b else print(f'{a} is greater than {b}') if a > b else print ('3')
#
# a = 1
# while a < 6:
#     print(a)
#     if a == 3:
#         break
# #     a += 1
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print('i is no longer less than 6')
# i = 0
# while i < 6:
#
#     i += 1
#     if i == 3:
#         continue
# #     print(i)
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#    if x == "banana":
#         continue
#    print(x)
# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print('hello')

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x, y)
# x = 'spam'
# while x:
#     print(x, end=" ")
#     x = x[1:]

# x = 10
# while x:
#     x = x - 1
#     if x % 2 != 0: continue
#     print(x, end=" ")
# x = 10
# while x:
#     x = x - 1
#     if x % 2 == 0:
#         print(x, end=' ')

# while 1:
#     name = input('Enter name ')
#     if name == 'Mary':
#         break
#     age = input('Enter age: ')
#     print('Hello', name, '=>', int(age) ** 2)

#
# x = 4
# y = 3
# while x > 1:
#     if x % y == 0:
#         print(y, 'has factor', x)
#         # break
#     x -= 1
#     print(x)
# else:
# #     print(y, 'is prime')
# x = 10
# match = [1, 2, 3]
# found = False
# while x and not found:
#     if match(x[0]):
#         print('Ni')
#         found = True
#     else:
#         x = x[1:]
# if not found:
#     print('not found')
# sum = 0
# for x in [1, 2, 3, 4]:
#     sum = sum + x
# print(sum)
#
# prod = 1
# for item in [1, 2, 3, 4]: prod *= item
# print(prod)

# S = 'lumberjack'
# T = ('and', 'I’m', 'okay')
# for x in S: print(x, end='')
# print(S)
# T = [(1, 2), (3, 4), (5, 6)]
# for (a, b) in T:  # Операция присваивания кортежа в действии
#     print(a, b)
# print(list(range( 5, -9)))

# Функции

# def times(x, y):
#     return x * y
# x = times(3.14, 4)
# print(x)
#
# def times(x, y):
#     return x * y
# print(times(1, 3))
# def  intersect(seq1, seq2):
#     res = []
#     for x in seq1:
#         if x in seq2:
#             res.append(x)
#     return(res)
# print(intersect(seq1=[1, 2, 3], seq2=(1, 2)))

# def muy_func():
#     print('hello')
# muy_func()
#
# def func(fname):
#     print(f'{fname} '+ 'Kapuza')
#
# func("Vitya")
# func("Olia")
#
# def my_function(fname, lname):
#     print(fname + " " + lname)
# my_function('Emma', 'Minkovich')

# def func(*kids):
#     print('The child is ' + kids[0])
# func('Emil', 'Nino')

# def fuc(country = 'Norway'):
#     print('I am from ' + country)
# fuc('India')
#
# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)
# def func(x):
#     return 5 * x
# print(func(4))
# print(func(5))
#
# from decimal import Decimal
#
# a = Decimal("0.1")
# print(a * 10)

# from decimal import Decimal
#
# a = Decimal('0.1')
# print(a)
#
# a = "abvd"
# print('abvd' * 3)
# print(len('abvd'))
# s = 'abcdef'
# print(s[::2])
#
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")
txt = ",,,,,ssaaww..               banana"

x = txt.lstrip(",.asw")

print(x)