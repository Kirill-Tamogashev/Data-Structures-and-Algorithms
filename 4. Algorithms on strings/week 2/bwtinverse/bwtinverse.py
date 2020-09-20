# python3
import sys


def InverseBWT(bwt):
    n = len(bwt)
    A, C, G, T = 1, 1, 1, 1
    l_Col = []
    for symbol in bwt:
        if symbol == '$':
            l_Col.append(('$', 0))
        elif symbol == 'A':
            l_Col.append(('A', A))
            A += 1
        elif symbol == 'C':
            l_Col.append(('C', C))
            C += 1
        elif symbol == 'G':
            l_Col.append(('G', G))
            G += 1
        elif symbol == 'T':
            l_Col.append(('T', T))
            T += 1
    f_Col = sorted(l_Col)

    f_To_l = {}
    for i in range(n):
        f_To_l[f_Col[i]] = l_Col[i]
    
    res = ''
    elem = ('$', 0)
    for i in range(n):
        res += elem[0]
        elem = f_To_l[elem]
    return res[::-1]

if __name__ == '__main__':
    bwt = input()
    print(InverseBWT(bwt))