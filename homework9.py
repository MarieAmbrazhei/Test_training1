""" Homework9: Functions writing and implementing programs
in Python """


# Последовательность
# Дана последовательность целых чисел в виде массива. Определите, можно ли
# получить строго возрастающую последовательность, удалив из массива не более
# одного элемента.
# Примечание: последовательность a0, a1, ..., an считается строго возрастающей,
# если a0 < a1 < ... < an. Последовательность, содержащая только один элемент,
# также считается строго возрастающей.
# Примеры
# Для последовательности = [1, 3, 2, 1], вывод должен быть решение = False.
# В этом массиве нет ни одного элемента, который можно было бы удалить, чтобы
# получить строго возрастающую последовательность.
# Для последовательности = [1, 3, 2] вывод должен быть = True.
# Вы можете удалить 3 из массива, чтобы получить строго возрастающую
# последовательность [1, 2]. Альтернативно можно убрать 2, чтобы получить
# строго возрастающую последовательность [1, 3].


def can_be_ascending_by_removing_one(seq_int):
    """
    Get a strictly ascending sequence by removing only one element.
    """
    count = 0

    for i in range(len(seq_int) - 1):
        if seq_int[i] >= seq_int[i + 1]:
            count += 1
            if count > 1:
                return False

            if i > 0 and seq_int[i - 1] >= seq_int[i + 1] and i + 2 < len(
                    seq_int) and seq_int[i] >= seq_int[i + 2]:
                return False

    return True


print(can_be_ascending_by_removing_one([1, 2, 3]))
print(can_be_ascending_by_removing_one([1, 2, 1, 2]))
print(can_be_ascending_by_removing_one([1, 3, 2, 1]))
print(can_be_ascending_by_removing_one([1, 2, 3, 4, 5, 3, 5, 6]))
print(can_be_ascending_by_removing_one([40, 50, 60, 10, 20, 30]))


# Число на против
# Рассмотрим целые числа от 0 до n-1, записанные по окружности так, чтобы
# расстояние между любыми двумя соседними числами было одинаковым (обратите
# внимание, что 0 и n-1 тоже являются соседними).
# Учитывая n и first_number, найдите число, которое написано в радиально
# противоположной позиции от first_number.
# Для n = 10 и first_number = 2 вывод должен быть (n, first_number) = 7.


def find_opposite_number(n, first_number):
    """
    Find the the radially opposite number.
    """
    degree_between_numbers = 360 / n
    opposite_number = (180 / degree_between_numbers + first_number) % n
    return int(opposite_number)


print(find_opposite_number(10, 9))

# Validate
# Ваша задача написать программу, принимающее число - номер кредитной карты
# (число может быть четным или не четным).
# И проверяющей может ли такая карта существовать. Предусмотреть защиту от
# ввода букв, пустой строки и т.д. Примечания Алгоритм Луна

from functools import reduce


def validate_card(card_number):
    """
    Validate a credit card number using the Luhn algorithm.
    """
    even = []
    odd = []
    card_number_reverted = card_number[::-1]
    for elem in range(len(card_number)):
        if (elem + 1) % 2 == 0:
            odd_number = int(card_number_reverted[elem]) * 2
            if odd_number > 9:
                odd_number -= 9
            odd.append(odd_number)

        else:
            even.append(card_number_reverted[elem])

    result = reduce(lambda x, y: x + y, [*list(map(int, even)),
                                         *odd])
    if result % 10 == 0:
        return True
    return False


print(validate_card('4561261212345464'.replace(' ', '')))
print(validate_card('4561261212345467'.replace(' ', '')))