import sys

def bipartite(adj):
    color = ['w'] * len(adj)
    dist = ['inf'] * len(adj)
    part = [0] * len(adj)

    color[0], dist[0], part[0] = 'g', 0, 1

    Q = [0]
    while Q:
        u = Q.pop(0)
        for v in adj[u]:
            if part[u] == part[v]:
                return 0
            elif color[v] == 'w':
                color[v] = 'g'
                dist[v] = dist[u] + 1
                part[v] = 3 - part[u]
                Q.append(v)
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))