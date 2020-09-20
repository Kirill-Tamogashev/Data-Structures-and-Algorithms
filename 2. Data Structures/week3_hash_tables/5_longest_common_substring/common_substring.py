# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def substring_lenth(s_1, s_2):
    l = 0, r = min(s_1, s_2)
    


def poliHash(S, p, x):
    p = 1000000009
    h = 0
    for s in reversed(S):
        h = (h * x + ord(s)) % p
    return h


def precomputeHashes(string, pp, x):
	p = 1000000009
    H = [None for _ in range(len(string) - pp + 1)]
    S = string[len(string) - pp:]
    H[len(string) - pp] = poliHash(S, p, x)
    y = 1
    for _ in range(1, pp + 1):
        y = (y * x) % p
    j = len(string) - pp -1
    while j >= 0:
        H[j] = (x * H[j+1] + ord(string[j]) - y * ord(string[j + pp])) % p
        j -= 1
    return H


def solve(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans

for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)

