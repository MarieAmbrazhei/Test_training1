"""Homework#6; Python data types: creating lists and using basic methods."""

# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
MY_FIRST_STR = "Robin Singh"
creating_first_list = MY_FIRST_STR.split()
print(creating_first_list)

# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
LONG_STRING = "I love arrays they are my favorite"
creating_long_list = LONG_STRING.split()
print(creating_long_list)

# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
first_list = ["Ivan", "Ivanou"]
STRING_ONE = "Minsk"
STRING_TWO = "Belarus"
final_list = first_list + [STRING_ONE, STRING_TWO]
print(final_list)

fullname_in_list = ["Ivan", "Ivanou"]
CITY_IN_STR = "Minsk"
COUNTRY_IN_STR = "Belarus"
general_names_in_list = []
general_names_in_list.extend(fullname_in_list + [CITY_IN_STR, COUNTRY_IN_STR])
print(general_names_in_list)

# Напечатайте текст: “Привет, Ivan Ivanou!
# Добро пожаловать в Minsk Belarus”
fullname_in_list = ["Ivan", "Ivanou"]
CITY_IN_STR = "Minsk"
COUNTRY_IN_STR = "Belarus"
print("Привет,", ' '.join(fullname_in_list) + "!", "Добро пожаловать в",
      CITY_IN_STR, COUNTRY_IN_STR)

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
list_of_words = ["I", "love", "arrays", "they", "are", "my", "favorite"]
STR_OF_WORDS = ' '.join(list_of_words)
print(STR_OF_WORDS)

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
list_of_ten_positions = ["one", 2, 0.5, {"a": "b"}, "python", [3, 6], 3,
                         "THE BEST", 8, 9, "5g"]
print("Длина:", len(list_of_ten_positions))
list_of_ten_positions.insert(3, "Awesome_python")
print(list_of_ten_positions)
del list_of_ten_positions[6]
print(list_of_ten_positions)
