# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    ops = []
    for i, next in enumerate(text):
        index = i + 1
        if next in "([{":
            # Process opening bracket, write your code here
            ops.append((next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if ops == []:
                return index
            top = ops[-1][0]
            ops.pop()
            if (top == '[' and next != ']') or \
                (top == '(' and next != ')') or \
                (top == '{' and next != '}'):
                return index

    if ops == []:
        return 'Success'
    return ops[0][1]

text = input()
print(find_mismatch(text))
