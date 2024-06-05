# from collections import Counter
#
# given_str = "cccbba"
# collections = Counter(given_str)
#
# print(collections)

# a_string = 'cccbba'
# print('a: ', a_string.count('a'))
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

# x = 'cccbba'
# y = []
# for i in x:
#     if i not in y:
#         y.append(i)
#
# print(''.join(y))

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
