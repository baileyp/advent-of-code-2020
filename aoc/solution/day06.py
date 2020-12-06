def part1(file):
    """
    O(n) space and time
    :param file:
    :return:
    """
    return sum(len(answers) for answers in group_answers_from_file(file))


def part2(file):
    return None


def group_answers_from_file(file):
    answers = set()

    for line in file:
        if line is '':
            yield answers
            answers = set()
            continue
        answers = answers.union(set(line))

    yield answers
