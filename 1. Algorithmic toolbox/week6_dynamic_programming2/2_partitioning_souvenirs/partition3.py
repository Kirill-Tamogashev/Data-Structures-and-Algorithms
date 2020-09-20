# Uses python3
import sys
import itertools

def partition3(W):
    w = sum(W)
    if w%3 != 0:
        return 0
    
    n = len(W)
    if n < 3:
        return 0
    
    w = w // 3


    value = []
    for _ in range(w + 1):
        m = [0] * (n + 1)
        value.append(m)
    count = 0
    for i in range(1, w + 1):
        for j in range(1, n + 1):
            value[i][j] = value[i][j - 1]
            if W[j - 1] <= i:
                val = value[i - W[j - 1]][j - 1] + W[j - 1]
                if val > value[i][j]:
                    value[i][j] = val
            if value[i][j] == w: count += 1
                
    if count < 3:
        return 0
    else:
        return 1 



n = int(input())
A = list(map(int, input().split()))
print(partition3(A))

