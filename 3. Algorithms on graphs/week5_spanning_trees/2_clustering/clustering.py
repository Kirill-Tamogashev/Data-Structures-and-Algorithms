import sys
import math


class Vetrex:
    def __init__(self, x, y, parent):
        self.r = 0
        self.x, self.y, self.p = x, y, parent


class Edge:
    def __init__(self, u, v, weight):
        self.w = weight
        self.u, self.v = u, v


def mSet(ver, x, y):
    for i in range(len(x)):
        ver.append(Vetrex(x[i], y[i], i))


def L(x_1, y_1,  x_2, y_2):
    return math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))


def find(r, ver):
    if ver[r].p != r:
        ver[r].p = find(ver[r].p, ver)
    return ver[r].p


def unite(v, w, ver):
    el_1 = find(v, ver) 
    el_2 = find(w, ver)
    if el_1 != el_2:
        if ver[el_1].r > ver[el_2].r:
            ver[el_2].p = el_1
        else:
            ver[el_1].p = el_2
            if ver[el_1].r == ver[el_2].r:
                ver[el_2].r += 1


def clustering(x, y, k):
    #write your code here
    ver = []
    mSet(ver, x, y)
    E_set = []

    for i in range(len(x)):
        for j in range(i+1, len(x)):
            E_set.append(Edge(i, j, L(x[i], y[i], x[j], y[j])))
    E_set.sort(key=lambda edge: edge.w)
    bar = 0
    for edge in E_set:
        if find(edge.u, ver) != find(edge.v, ver):
            bar += 1
            unite(edge.u, edge.v, ver)
            if bar > len(x) - k:
                return edge.w, E_set
    return -1.


if __name__ == '__main__':
    #input = sys.stdin.read()
    data = list(map(int, input().split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))