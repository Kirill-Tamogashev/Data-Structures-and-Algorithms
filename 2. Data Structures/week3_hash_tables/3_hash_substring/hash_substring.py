import random

def poliHash(S, p, x):
    h = 0
    for s in reversed(S):
        h = (h * x + ord(s)) % p
    return h

def precomputeHashes(text, pp, p, x):
    H = [None for _ in range(len(text) - pp + 1)]
    S = text[len(text) - pp:]
    H[len(text) - pp] = poliHash(S, p, x)
    y = 1
    for _ in range(1, pp + 1):
        y = (y * x) % p
    j = len(text) - pp -1
    while j >= 0:
        H[j] = (x * H[j+1] + ord(text[j]) - y * ord(text[j + pp])) % p
        j -= 1
    return H

def get_occurrences(pattern, text):
    p = 49979687
    x = random.randint(1, p - 1) 
    results = []
    pHash = poliHash(pattern, p, x)
    H = precomputeHashes(text, len(pattern), p, x)
    for i in range(len(text) - len(pattern) + 1):
        if pHash == H[i]:
            if text[i: i + len(pattern)] == pattern:
                results.append(i)
    return results 



def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

