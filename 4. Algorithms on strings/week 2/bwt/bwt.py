# python3
import sys


def BWT(text):
    result = []
    n = len(text)
    for _ in range(n):
        last, rem = text[n - 1], text[:n - 1]
        text = last + rem
        result.append(text)
    result.sort()
    print(''.join([result[i][-1] for i in range(n)]))


if __name__ == '__main__':
    #text = sys.stdin.readline().strip()
    text = input()
    BWT(text)