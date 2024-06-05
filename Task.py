# 1напишите функцию, которая возвращает строку: 'Hello world'
# def greet():
#     return 'Hello world'
# print(greet())
import time
from datetime import datetime as dt


# 2напишите функцию, которая вычисляет сумму
# трех числе и возвращает результат в основную ветку программы.

# def calc(a, b, c):
#     return a + b + c
# print(calc(1, 2, 3))

# 3 программа, в которой из одной функции вызывается вторая.
# При этом ни одна из них ничего не возвращает в
# овсновную ветку программы. обе должны выводить рекз-таты своей
# работы с помощью print.
# def calc(a, b, c):
#     return a + b + c
#
# def input_pls():
#     a = int(input("Please enter number a:  "))
#     b = int(input("Please enter number b: "))
#     c = int(input("Please enter number c: "))
#     print(calc(a, b, c))
#
#
# input_pls()

# def func2():
#     print("it's print from func2")
#
#
# def func1(func):
#     print("it's print from func1")
#     func()


# func1(func=func2)

# 4. Напишите функцию, которая не принимает отрицательные числа. и возвращает
# число наоборот.
# 21445 => 54421
# 123456789 => 987654321

# def reverse_str(numb):
#     if numb >= 0:
#         return int(str(numb)[::-1])
#
#     print(f'Given number {numb} less than zero')
#     return False
#
#
# print(reverse_str(numb=-21445))

# 5. У вас интернет магазин, надо написать функцию, которая проверяет,
# что введен правильный купон и он еще
#  действителен:


#
#
# def check_coupon(entered_code, correct_code, current_date, expiration_date):
#     # Преобразование строковых дат в объекты datetime для сравнения
#     current_date_obj = dt.strptime(current_date, "%B %d, %Y")
#     expiration_date_obj = dt.strptime(expiration_date, "%B %d, %Y")
#     if entered_code == correct_code and current_date_obj <= expiration_date_obj:
#         return True
#     return False
#
#
# print(check_coupon(entered_code="123", correct_code="123",
#                    current_date="July 9, 2015",
#                    expiration_date="July 8, 2015"))
# print(check_coupon(entered_code="123", correct_code="123",
#                    current_date="July 9, 2015",
#                    expiration_date="July 9, 2015"))

#
#
# def change(a):
#     b = a[:]
#     a.append(1)
#     print(a)
#     print(b)
#
# change(a)
# print(a)
#
# arr = list(range(10))
#
# def is_even(n):
#     return n % 2 == 0
#
# print(list(filter(is_even, arr)))
#
# print([el for el in arr if is_even(el)])

# def print_stars(number):
#     for elem in range(1, number, 2):
#         spaces = int((number - elem) / 2)
#         print(f'{" "  spaces}{"*"  elem}{" " * spaces}')
#
#
# print_stars(10)
# def print_stars(number):
#     for elem in range(1, number, 1):
#         spaces = int((number - elem) / 2)
#         print(f'{" " * spaces}{"*" * elem}{" " * spaces}')
#
#
# print_stars(10)
# def print_stars(number):
#     start_string = ' ' * (number * 2 + 1)
#     for elem in range(0, number):
#         stars = '*' * (elem * 2 + 1)
#         spaces = ' ' * int((len(start_string) - len(stars)) / 2)
#         print(f'{spaces}{stars}{spaces}')
#
#
# print_stars(10)

# Напишите функцию декоратор, которая добавляет 1 к заданному числу
# def add_number(func):
#     def add_number2(a):
#         a += 1
#         func(a)
#
#     return add_number2
#
#
# @add_number
# def sum(a):
#     print(a)
#
#
# sum(1)


# def add_number(func):
#     def add_number2(a: str):
#         a = a.upper()
#         func(a)
#
#     return add_number2
#
#
# @add_number
# def text(a):
#     print(a)
#
#
# text("qwerty")

# Напишите функции декораторы, которые форматируют текст(добавляют
# html теги) в различные стили:
# Жирный <b> </b>
# Курсив <i> </i>
# Подчеркивание <u> </u>

#
# def bold_reg(reg):
#     def wrapper(text1: str):
#         a = f'<b>{text1}</b>'
#         reg(a)
#
#     return wrapper
#
#
# def ita_reg(reg):
#     def wrapper(text1: str):
#         a = f'<i>{text1}</i>'
#         reg(a)
#
#     return wrapper


# def under_reg(reg):
#     def wrapper(text1: str):
#         a = f'<u>{text1}</u>'
#         reg(a)
#
#     return wrapper
#
#
# @under_reg
# @ita_reg
# @bold_reg
# def reg(text):
#     print(text)
#
#
# reg("hello")
#
# a = "10, 20, 30, 40"
# elem = a.split(', ')
# for i, elem in enumerate(elem):
#     print(i, elem)

# msg = "This is a test message"
#
# arr = msg.split(" ")
# print(arr)


# - Фильтр. Функция принимает на вход список, проверяет есть ли эти элементы в
# списке exclude, если есть удаляет их и возвращает список с оставшимися элементами
# exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# filter_list(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse",
# "Blue Swedish"]) => ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"] => ["Mallard",
# "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
# ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"] => []

# def filter_i(filter_list, exclude):
#     for i in exclude:
#         if i in filter_list:
#            filter_list.remove(i)
#     print(filter_list)
#
#
# filter_list = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse",
#  "Blue Swedish"]
# exclude = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
#
# print(filter_i(filter_list, exclude))

# Напишите функцию, которая проверяет на то, является ли строка палиндромом или
# нет. Палиндром —
# это слово или фраза, которые одинаково читаются слева направо и справа налево.

# def check_is_palindrope(string):
#     reversed_str = string[::-1]
#     if string == reversed_str:
#         return (f'{string} is palindrope')
#
#     print(f'{string} is not palindrope')
#     return False
#
#
# string = "дед"
# print(check_is_palindrope(string))


# def is_palindrom(data):
#     if data == data[::-1]:
#         return True
#     return False
#
#
# assert is_palindrom('qwerty') == False, 'Не является палиндромом'
# assert is_palindrom('level') == True
#
# print(is_palindrom(data='дед'))

# def to_square(a):
#     return a ** 2
#
#
# numbers = [1, 2, 3, 4]
#
# print(list(map(to_square, numbers)))
# # print([to_square(item) for item in numbers])
#
# def can_be_ascending_by_removing_one(seq_int):
#     new_arr = sorted(seq_int[:])
#     counter = 0
#
# def remove_excessive(new_arr):
#     nonlocal counter
#     if counter <= 1:
#         for i in range(len(new_arr) - 1):
#
#             if new_arr[i] >= new_arr[i + 1]:
#                 del new_arr[i]
#                 # print(new_arr)
#                 counter += 1
#                 if counter > 1:
#                     return False
#
# remove_excessive(new_arr)
# if counter < 1:
#     return True
# return False
# return remove_excessive(new_arr)
#
# def can_be_ascending_by_removing_one(arr):
#     if (len(arr) - len(set(arr))) > 1:
#         return False
#     for i in range(len(arr) - 1):
#         if new_arr[i] >= new_arr[i + 1]:
#
#
#
# print(can_be_ascending_by_removing_one([1, 2, 3]))
# print(can_be_ascending_by_removing_one([1, 2, 1, 2]))
# print(can_be_ascending_by_removing_one([1, 3, 2, 1]))
# print(can_be_ascending_by_removing_one([1, 2, 3, 4, 5, 3, 5, 6]))
# print(can_be_ascending_by_removing_one([40, 50, 60, 10, 20, 30]))

# def find_opposite_number(n, first_number):
#     degree_between_numbers = 360 / n
#     opposite_number = (180 / degree_between_numbers + first_number) % n
#     return int(opposite_number)
#
#
# print(find_opposite_number(10, 7))

#
# def can_be_ascending_by_removing_one(seq_int):
#     count = 0
#
#     for i in range(len(seq_int) - 1):
#         if seq_int[i] >= seq_int[i + 1]:
#             count += 1
#             if count > 1:
#                 return False
#
#
#             if i > 0 and seq_int[i - 1] >= seq_int[i + 1] and i + 2 < len(seq_int) and seq_int[
#                 i] >= seq_int[i + 2]:
#                 return False
#
#     return True
#
#
# # Примеры использования
# print(can_be_ascending_by_removing_one([1, 2, 3]))  # True
# print(can_be_ascending_by_removing_one([1, 2, 1, 2]))  # False
# print(can_be_ascending_by_removing_one([1, 3, 2, 1]))  # False
# print(can_be_ascending_by_removing_one([1, 2, 3, 4, 5, 3, 5, 6]))  # True
# print(can_be_ascending_by_removing_one([40, 50, 60, 10, 20, 30]))  # False

# def solution(nums):
#     """
#     Checks whether a strictly increasing sequence can be obtained,
#     removing at most one element from the array.
#     """
#     def is_increasing(nums):
#         """
#         Is the array of numbers increasing.
#         """
#         for i in range(len(nums)-1):
#             if nums[i] >= nums[i+1]:
#                 return False
#         return True
#
#     for i in range(len(nums)):
#         temp = nums[:i] + nums[i+1:]
#         if is_increasing(temp):
#             return True
#     return False
#
#
# print(solution([1, 2, 3]))
# print(solution([1, 2, 1, 2]))
# print(solution([1, 3, 2, 1]))
# print(solution([1, 2, 3, 4, 5, 3, 5, 6]))
# print(solution([40, 50, 60, 10, 20, 30]))

# def validate(card):
#     summ = 0
#     cardnumbers = [int(elem) for elem in card]
#     for i in range(len(cardnumbers)):
#         num = cardnumbers[i]
#         if i % 2 == 0:
#             even = num * 2
#             if even > 9:
#                 even -= 9
#                 summ += even
#         else:
#             summ += num
#
#     return summ % 10 == 0
#
#
# print(validate('4561261212345467'))
# from functools import reduce
#
# def validate_card(card_number):
#     even = []
#     odd = []
#     card_number_reverted = card_number[::-1]
#     for elem in range(len(card_number)):
#         if (elem + 1) % 2 == 0:
#             odd_number = int(card_number_reverted[elem]) * 2
#             if odd_number > 9:
#                 odd_number -= 9
#             odd.append(odd_number)
#
#         else:
#             even.append(card_number_reverted[elem])
#
#     result = reduce(lambda x, y: x + y, [*list(map(int, even)), *odd])
#     if result % 10 == 0:
#         return True
#     return False
#
#
# print(validate_card('5062 8212 3456 7892'.replace(' ', '')))
# from functools import reduce
#
#
# def validate_card(card_number: str) -> bool:
#     """
#     Validate a credit card number using the Luhn algorithm.
#     """
#     even = []
#     odd = []
#     card_number_reverted = card_number[::-1]
#     for elem in range(len(card_number)):
#         if (elem + 1) % 2 == 0:
#             odd_number = int(card_number_reverted[elem]) * 2
#             if odd_number > 9:
#                 odd_number -= 9
#             odd.append(odd_number)
#
#         else:
#             even.append(int(card_number_reverted[elem]))
#
#     validation_sum = reduce(lambda x, y: x + y, even + odd)
#     if validation_sum % 10 == 0:
#         return True
#     return False
#
#
# print(validate_card('4561261212345464'.replace(' ', '')))
# print(validate_card('4561261212345467'.replace(' ', '')))

# Напишите программу. Есть 2 переменные salary и bonus.
# Salary - integer, bonus - boolean. Если bonus - true, salary должна
# быть умножена на 10. Если false - нет
# 10000, True == '$100000'
# 25000, True == '$250000'
# 10000, False == '$10000'
# 60000, False == '$60000'
# 2, True == '$20'
# 78, False == '$78'
# 67890, True == '$678900'

# def check_bonus(salary: int, bonus: bool) -> str:


# if bonus:
#         return f'${salary * 10}'
#     return f'${salary}'
#
#
#
# print(check_bonus(salary=2, bonus=False))
# print(check_bonus(salary=3, bonus=True))
# print(check_bonus(2,True))
# def check_bonus(salary: int, bonus: bool) -> str:
#     return f'${salary * 10}' if bonus else f'${salary}'
#
#
# print(check_bonus(2, True))
# "a#bc#d" ==>  "bd"
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""


# def remove_excessive_symbols(str_with_hash: str) -> str:
#     try:
#         while str_with_hash.index('#'):
#             index = str_with_hash.index('#')
#             str_with_hash = str_with_hash[:index-1] + str_with_hash[index+1:]
#     except ValueError:
#         return str_with_hash
#
#
# print(f"'{remove_excessive_symbols('a#bc#d')}'")
# print(f"'{remove_excessive_symbols('abc#d##c')}'")
# print(f"'{remove_excessive_symbols('abc##d######')}'")
# print(f"'{remove_excessive_symbols('#######')}'")
# print(f"'{remove_excessive_symbols('')}'")
# Строки с заданным символом
# Напишите программу, которая бы работала следующим образом - находила символ
# "#" и если этот символ найден - удаляла предыдущий символ из строки. Ваша
# задача обработать строки с "#" символом

# def remove_excessive_symbols(str_with_hash: str) -> str:
#     while True:
#         try:
#             index = str_with_hash.index('#')
#             if index > 0:
#
#                 str_with_hash = str_with_hash[:index-1] + str_with_hash[index+1:]
#             else:
#
#                 str_with_hash = str_with_hash[index+1:]
#         except ValueError:
#             break
#     return str_with_hash
#
# print(f"'{remove_excessive_symbols('a#bc#d')}'")
# print(f"'{remove_excessive_symbols('abc#d##c')}'")
# print(f"'{remove_excessive_symbols('abc##d######')}'")
# print(f"'{remove_excessive_symbols('#######')}'")
# print(f"'{remove_excessive_symbols('')}'")
# # верно

# def remove_excessive_symbols(str_with_hash: str) -> str:
#     try:
#         while str_with_hash.index('#'):
#             index = str_with_hash.index('#')
#             str_with_hash = str_with_hash[:index-1] + str_with_hash[index+1:]
#     except ValueError:
#         return str_with_hash
#
#
# print(f"'{remove_excessive_symbols('a#bc#d')}'")
# print(f"'{remove_excessive_symbols('abc#d##c')}'")
# print(f"'{remove_excessive_symbols('abc##d######')}'")
# print(f"'{remove_excessive_symbols('#######')}'")
# print(f"'{remove_excessive_symbols('')}'")

# def make_new_candels(candles_number, make_new):
#     total_burned = 0
#     left_overs = 0
#
#     while candles_number > 0:
#         total_burned += candles_number
#         left_overs += candles_number
#         candles_number = left_overs // make_new
#         left_overs = left_overs % make_new
#     return total_burned
#
#
# print(make_new_candels(3, 2))
# верно
# Подсчет количества букв
# На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
#
# Примеры для проверки работоспособности:
#
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"
#
# from collections import Counter
#
# given_str = "cccbba"
# collections = Counter(given_str)
#
# print(collections)

# a_string = 'cccbba'
# print('a: ', a_string.count('a'))


# array = ["Bob", "Alex", "Bob", "John"]
#
# array_d = {}.fromkeys(array, 0)
# for a in array:
#     array_d[a] += 1
#
# # print(array_d)
#
# s = "abcde"
# result = ""
# rep = set()
# for x in s:
#     if x not in rep:
#         result += f"{x}{s.count(x)}"
#         a = result.replace('1', "" )
#         rep.add(x)
#     else:
#         result += x
# print(result)

# def count_letters(input_string):
#     result = ""
#
#     for char in input_string:
#         count = input_string.count(char)
#         # rep = set()
#
#         if count > 1:
#             for i in sorted(set(count)):
#                 result += char + str(count)
#
#         else:
#
#             result += char
#
#     return result
#
#
# print(count_letters("cccbba"))
# print(count_letters("abeehhhhhccced"))
# print(count_letters("aaabbceedd"))
# print(count_letters("abcde"))
# print(count_letters("aaabbdefffff"))

#
# x = 'cccbba'
# y = []
# for i in x :
#     if i not in y:
#         y.append(i)
#
# print(''.join(y))


# def stringcount(incoming_str):
#     enumerator = 0
#     incoming_str += ' '
#     result = ''
#     for a in range(len(incoming_str) - 1):
#         enumerator += 1
#         letter = incoming_str[a]
#         if incoming_str[a] != incoming_str[a + 1]:
#             result += letter
#             if enumerator > 1:
#                 result += str(enumerator)
#             enumerator = 0
#     return result
#
# TEXT = 'cccbba'
# print(stringcount(TEXT))


# def letter_count(user_str):
#     count_let = 1
#     result = ''
#     for key, value in enumerate(user_str):
#         if key == len(user_str) - 1:
#             if count_let == 1:
#                 result += user_str[key]
#             else:
#                 result += user_str[key] + str(count_let)
#             break
#         if user_str[key] == user_str[key + 1]:
#             count_let += 1
#         else:
#             if count_let == 1:
#                 result += user_str[key]
#             else:
#                 result += user_str[key] + str(count_let)
#             count_let = 1
#     return result
#
#
# print(letter_count("cccbba"))

# апишите функцию на вход которой подается строка, например, "cccbba"
# # результат работы программы - строка “c3b2a"
# # Примеры для проверки работоспособности:
# # "cccbba" == "c3b2a"
# # "abeehhhhhccced" == "abe2h5c3ed"
# # "aaabbceedd" == "a3b2ce2d2"
# # "abcde" == "abcde"
# # "aaabbdefffff" == "a3b2def5"
#
# STRING = "abeehhhhhccced"

#
#


#
# def count_letters(given_string):
#     result_string = ''
#     letters = {}
#
#     def count_and_remove(cut_string):
#         nonlocal result_string, letters
#         for idx, letter in enumerate(cut_string):
#             if letter not in letters:
#                 letters[letter] = 1
#             else:
#                 letters[letter] += 1
#             if len(cut_string) == 1 or len(set(cut_string)) == 1:
#                 result_string += (letter + str(len(cut_string)))
#                 return result_string.replace('1', '')
#             if cut_string[idx] != cut_string[idx + 1]:
#                 result_string += (letter + str(letters.get(letter)))
#                 cut_string = cut_string[idx + 1:]
#                 letters = {}
#                 return count_and_remove(cut_string)
#
#     return count_and_remove(given_string)
#
#
# assert count_letters('cccbba') == "c3b2a"
# assert count_letters('abeehhhhhccced') == "abe2h5c3ed"
# assert count_letters('aaabbceedd') == "a3b2ce2d2"
# assert count_letters('abcde') == "abcde"
# assert count_letters('aaabbdefffff') == "a3b2def5"

# for  elem in range(1, 4):
#     print(elem)
# a, *c, b = (1, 3, 4, 5, 2)
# print(c)
# for el in enumerate('abcd'):
#     print(el)

# m_dict = {'a': 1, 'b': 2, 'c': 3}
# print(m_dict.get('b'))
# print(m_dict['b'])
# m_dict['b'] += 1
# print(m_dict)
# m_dict['v'] = '4'
# print(m_dict)
# m_dict.update({'w': 5})
# print(m_dict)
# m_dict.update({'b': 5})
# print(m_dict)