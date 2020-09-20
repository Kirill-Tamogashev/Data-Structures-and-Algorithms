#!/usr/bin/python3

import sys
import queue

class BiDij:
    def __init__(self, n):
        self.n = n                              # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [False]*n                # visited[v] == True iff v was visited by forward or backward search
        self.workset = []                       # All the nodes visited by forward or backward search


    def clear(self):
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visited[v] = False
        del self.workset[0:len(self.workset)]


    def visit(self, q, side, v, dist):
        if self.d[side][v] > dist:
            self.d[side][v] = dist
            q[side].put((self.d[side][v], v))
            self.workset.append(v)


    def query(self, adj, cost, s, t):
        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.visit(q, 0, s, 0)
        self.visit(q, 1, t, 0)

        while not q[1].empty() and not q[0].empty():
            for i in [0, 1]:
                u = q[i].get()[1]
                for v, w in zip(adj[i][u], cost[i][u]):
                    self.visit(q, i, v, self.d[i][u] + w)
                if self.visited[u] == True:
                    return self.path(v)
                self.visited[u] = True

        return -1


    def path(self, vertex):
        dist = self.inf

        for vertex in self.workset:
            if dist > self.d[0][vertex] + self.d[1][vertex]:
               dist = self.d[0][vertex] + self.d[1][vertex]

        if dist == self.inf:
            return -1
        return dist


def readl():
    return map(int, input().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))
