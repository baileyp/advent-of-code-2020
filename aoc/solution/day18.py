from collections import deque


def part1(file):
    """
    O(n * l) time and O(n + l) space where n is the number of input expressions and l is the length of the largest
    expression
    :param file:
    :return:
    """
    results = []
    for line in file:
        results.append(solve_expression(line.replace(' ', '')))

    return sum(results)


def part2(file):
    return None


def solve_expression(expression):
    stack = deque()
    left = 0
    while left < len(expression):
        atom = expression[left]
        if atom == '(':
            right = find_balanced(expression, left)
            stack.append(solve_expression(expression[left+1:right]))
            left = right
        else:
            stack.append(int(atom) if atom not in '+*' else atom)
        left += 1

    result = stack.popleft()
    while len(stack):
        atom = stack.popleft()
        if atom == '+':
            result += stack.popleft()
        elif atom == '*':
            result *= stack.popleft()

    return result


def find_balanced(expression, start_index):
    stack = deque()
    for i in range(start_index, len(expression) + 1):
        atom = expression[i]
        if atom == ')':
            stack.popleft()
        if atom == '(':
            stack.append('(')
        if len(stack) == 0:
            return i
    return None
