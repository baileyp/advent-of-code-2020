import re


def part1(file):
    """
    O(a) space and O(n) time where n is the number of lines in the program and a is the memory address space
    :param file:
    :return:
    """
    mask = ''
    memory = dict()
    for line in file:
        is_mask, data = parse_line(line)
        if is_mask:
            mask = data
        else:
            address, value = data
            memory[address] = apply_mask(int(value), mask)

    return sum(memory.values())


def part2(file):
    return None


def parse_line(line):
    if re.match(r"^mask", line):
        return True, line[7:]
    return False, re.findall(r"(\d+)\D+(\d+)", line).pop()


def apply_mask(number, mask):
    place = 0
    while place < 36:
        mask_bit = mask[35 - place]
        if mask_bit == 'X':
            place += 1
            continue
        number = int_to_bin_list(number)
        number[-(place + 1)] = mask_bit
        number = bin_list_to_int(number)

        place += 1

    return number


def int_to_bin_list(number, width=36):
    bin_list = list(bin(number))[2:]
    return [*['0' for _ in range(width - len(bin_list))], *bin_list]


def bin_list_to_int(bin_list):
    return int(''.join(bin_list), 2)

