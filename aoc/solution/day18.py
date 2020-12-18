from collections import deque
from functools import reduce


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
    """
    O(n * l) time and O(n + l) space where n is the number of input expressions and l is the length of the largest
    :param file:
    :return:
    """
    results = []
    for line in file:
        results.append(solve_expression(line.replace(' ', ''), addition_then_multiplication_solver))

    return sum(results)


def left_to_right_solver(stack: deque):
    result = stack.popleft()
    while len(stack):
        atom = stack.popleft()
        if atom == '+':
            result += stack.popleft()
        elif atom == '*':
            result *= stack.popleft()

    return result


def addition_then_multiplication_solver(stack: deque):
    while '+' in stack:
        stack.rotate(-stack.index('+'))
        stack.popleft()
        stack.appendleft(stack.popleft() + stack.pop())

    return reduce((lambda x, y: x * y), (n for n in stack if n != '*'))


def solve_expression(expression, solver=left_to_right_solver):
    stack = deque()
    left = 0
    while left < len(expression):
        atom = expression[left]
        if atom == '(':
            right = find_balanced(expression, left)
            stack.append(solve_expression(expression[left+1:right], solver))
            left = right
        else:
            stack.append(int(atom) if atom not in '+*' else atom)
        left += 1

    return solver(stack)


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
