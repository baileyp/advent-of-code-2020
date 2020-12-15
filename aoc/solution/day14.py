import re
from itertools import product


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
            address, value = (int(v) for v in data)
            for new_address in addresses_from_mask(address, mask):
                memory[new_address] = value

    return sum(memory.values())


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


def apply_mask_v2(number, mask):
    place = 0
    number_as_mask = int_to_bin_list(number)
    while place < 36:
        mask_bit = mask[35 - place]
        if mask_bit == '0':
            place += 1
            continue
        number_as_mask[-(place + 1)] = mask_bit

        place += 1

    return number_as_mask


def int_to_bin_list(number, width=36):
    bin_list = list(bin(number))[2:]
    return [*['0' for _ in range(width - len(bin_list))], *bin_list]


def bin_list_to_int(bin_list):
    return int(''.join(bin_list), 2)


def addresses_from_mask(address, mask):
    floating = {k: v for k, v in dict(enumerate(mask)).items() if v == 'X'}
    new_address = apply_mask_v2(address, mask)

    for permutation in product('01', repeat=len(floating)):
        diffs = zip(floating.keys(), permutation)
        for place, value in diffs:
            new_address[place] = value
        yield bin_list_to_int(new_address)
