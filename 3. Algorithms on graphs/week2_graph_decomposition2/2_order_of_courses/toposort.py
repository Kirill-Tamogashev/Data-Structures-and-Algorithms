import sys

def DFS(x, adj, used, order):
    used[x] = 1
    for i in range(len(adj[x])):
        if used[adj[x][i]] == 0:
            DFS(adj[x][i], adj, used, order)
    order.append(x)



def toposort(adj):
    order = []
    used = [0] * len(adj)
    
    for i in range(len(adj)):
        if used[i] == 0:
            DFS(i, adj, used, order)
    order.reverse()
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

