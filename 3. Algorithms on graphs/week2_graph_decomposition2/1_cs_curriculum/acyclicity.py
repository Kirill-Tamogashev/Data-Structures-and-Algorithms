import sys


def DFS(x, adj):
    global vis, stac
    vis[x] = 1
    stac[x] = 1

    for v in range(len(adj[x])):
        if not vis[adj[x][v]] and DFS(adj[x][v], adj):
            return 1
        elif stac[adj[x][v]]:
            return 1
    stac[x] = 0
    return 0


def acyclic(adj):
    global vis
    for x in range(len(adj)):
        if not vis[x]:
            if DFS(x, adj):
                return 1
    return 0


    
if __name__ == '__main__':
    #input = sys.stdin.read()
    data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    vis = [0 for _ in range(len(adj))]
    stac = [0 for _ in range(len(adj))]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))


