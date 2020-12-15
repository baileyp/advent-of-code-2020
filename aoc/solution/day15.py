from collections import defaultdict, deque


def part1(file, nth_spoken=2020):
    """
    O(n) time and O(s) space where n is the nth number to be spoken and s is the quantity of numbers spoken
    :param file:
    :param nth_spoken:
    :return:
    """
    starting_numbers = (int(n) for n in file.single_line().split(','))
    spoken = defaultdict(lambda: deque((0, 0)))

    game_round = 1
    last_spoken = None

    for number in starting_numbers:
        spoken[number].pop()
        spoken[number].appendleft(game_round)
        last_spoken = number
        game_round += 1

    while game_round < nth_spoken + 1:
        number_to_speak = 0
        if spoken[last_spoken][1] != 0:
            number_to_speak = max(spoken[last_spoken][0] - spoken[last_spoken][1], 1)

        spoken[number_to_speak].pop()
        spoken[number_to_speak].appendleft(game_round)
        last_spoken = number_to_speak
        game_round += 1

    return last_spoken


def part2(file):
    return part1(file, 30000000)
