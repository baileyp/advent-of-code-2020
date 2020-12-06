def part1(file):
    """
    O(n) space and time
    :param file:
    :return:
    """
    return sum(len(answers) for answers in group_answers_from_file(file))


def part2(file):
    """
    O(n) space and time
    :param file:
    :return:
    """
    return sum(len(answers) for answers in group_consensus_answers_from_file(file))


def group_answers_from_file(file):
    answers = set()

    for line in file:
        if line is '':
            yield answers
            answers = set()
            continue
        answers |= set(line)

    yield answers


def group_consensus_answers_from_file(file):
    all_answers = [chr(code) for code in range(97, 123)]
    answers = set(all_answers)

    for line in file:
        if line is '':
            yield answers
            answers = set(all_answers)
            continue
        answers &= set(line)

    yield answers
