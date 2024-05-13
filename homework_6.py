# """Homework#6; Python data types: creating lists and using basic methods."""

# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
my_first_string = "Robin Singh"
creating_first_list = my_first_string.split()
print(creating_first_list)

#"I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
long_string = "I love arrays they are my favorite"
creating_long_list = long_string.split()
print(creating_long_list)

# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
first_list = ["Ivan", "Ivanou"]
string_one = "Minsk"
string_two = "Belarus"
final_list = first_list + [string_one, string_two]
print(final_list)

fullname_in_list = ["Ivan", "Ivanou"]
city_in_str = "Minsk"
country_in_str = "Belarus"
general_names_in_list = []
general_names_in_list.extend(fullname_in_list + [city_in_str, country_in_str])
print(general_names_in_list)

# Напечатайте текст: “Привет, Ivan Ivanou!
# Добро пожаловать в Minsk Belarus”
fullname_in_list = ["Ivan", "Ivanou"]
city_in_str = "Minsk"
country_in_str = "Belarus"
print("Привет,", ' '.join(fullname_in_list) + "!", "Добро пожаловать в", city_in_str, country_in_str)

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
list_of_words = ["I", "love", "arrays", "they", "are", "my", "favorite"]
str_of_words = ' '.join (list_of_words)
print(str_of_words)

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
list_of_ten_positions = ["one", 2, 0.5, {"a": "b"}, "python", [3,6], 3, "THE BEST", 8, 9, "5g"]
print("Длина:", len(list_of_ten_positions))
list_of_ten_positions.insert(3, "Awesome_python")
print(list_of_ten_positions)
del list_of_ten_positions[6]
print(list_of_ten_positions)