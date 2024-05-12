# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
str_to_update = 'www.my_site.com#about'
print(str_to_update.replace('#', "/"))
# Напишите программу, которая добавляет ‘ing’ к словам
given_words = ["do", "go", "join"]
ing_addition = "ing"
for word in given_words:
    print(word + ing_addition)
# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
name_to_update = 'Ivanou Ivan'
print(' '.join(name_to_update.split()[::-1]))
# Напишите программу которая удаляет пробел в начале, в конце строки
words_with_spaces = ['    spaces_before_word', 'spaces_after_word    ']
print([word.strip() for word in words_with_spaces])
# Имена собственные всегда начинаются с заглавной буквы, за которой
# следуют строчные буквы. Исправьте данное имя собственное так,
# чтобы оно соответствовало этому утверждению.
# "pARiS" >> "Paris"
camel_case_names = ['pARiS', 'mOSCOw', 'pYthoNIsAwesOMe']
print([word.title() for word in camel_case_names])
