""" Homework8: Flow Control. Loops: writing and implementing programs
in Python """

# Быки и коровы
# В классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумывает и записывает тайное 4-значное число
# с неповторяющимися цифрами. Игрок, который начинает игру по жребию,
# делает первую попытку отгадать число. Попытка — это 4-значное число
# с неповторяющимися цифрами, сообщаемое противнику. Противник сообщает
# в ответ, сколько цифр угадано без совпадения с их позициями в тайном
# числе (то есть количество коров) и сколько угадано вплоть до позиции в
# тайном числе (то есть количество быков). При игре против компьютера
# игрок вводит комбинации одну за другой, пока не отгадает всю
# последовательность.
# Ваша задача реализовать программу, против которой можно сыграть в
# "Быки и коровы"

from random import choice

DIGITS = '0123456789'
RANDOM_DIGITS = choice(DIGITS[1:10])
for elements in range(3):
    DIGITS = ''.join(DIGITS.split(RANDOM_DIGITS[elements]))
    RANDOM_DIGITS += choice(DIGITS)
N = 0
while True:
    hidden_four_digit_num = input("ENTER A FOUR-DIGIT NUMBER: ")
    N += 1
    BULLS = 0
    COWS = 0
    for elements in range(4):
        if RANDOM_DIGITS[elements] == hidden_four_digit_num[elements]:
            BULLS += 1
        elif hidden_four_digit_num[elements] in RANDOM_DIGITS:
            COWS += 1
    print(hidden_four_digit_num + ' contain ' + str(BULLS) + ' bull and ' +
          str(COWS) + ' cows')
    if BULLS == 4:
        print('You won in ', N, 'steps')
        break


# Пирамида
# Мы можем визуализировать художественную пирамиду ASCII с N уровнями,
# напечатав
# N рядов звездочек, где верхний ряд имеет одну звездочку
# в центре, а каждый последующий ряд имеет две дополнительные звездочки с
# каждой
# стороны.
# Необходимо написать программу, которая генерирует такую
# пирамиду пирамиду со значением N, равным 10

def generate_pyramid(levels):
    """
    Wtite a program that generates a pyramid
    """
    for i in range(levels):
        spaces = " " * (levels - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)


generate_pyramid(10)


# Статуи
# Вы получили в подарок на день рождения статуи разных размеров, каждая статуя
# имеет неотрицательный целочисленный размер. Поскольку Вам нравится доводить
# вещи до совершенства, то необходимо расположить их от меньшего к большему,
# чтобы каждая статуя была больше предыдущей ровно на 1. Для этого Вам могут
# понадобиться дополнительные статуи. Определите количество отсутствующих
# статуй.
#
# Пример Для статуй = [6, 2, 3, 8] результат должен быть = 3. Иными словами, у
# Вас отсутствуют статуи размеров 4, 5 и 7.

def count_statues(statues_list):
    """
    Count missing statues in a sequence.
    """
    min_statue = min(statues_list)
    max_statue = max(statues_list)

    all_statues = list(range(min_statue, max_statue + 1))

    missing_statues = [statue for statue in all_statues if
                       statue not in statues_list]

    return len(missing_statues)


statues = [6, 2, 3, 8]
print(count_statues(statues))
