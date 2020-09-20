#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    a.sort(reverse=True)
    b.sort(reverse=True)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(max_dot_product(a, b))