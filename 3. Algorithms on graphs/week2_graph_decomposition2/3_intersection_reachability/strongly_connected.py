import sys


sys.setrecursionlimit(200000)

def DFS(x, adj, used, postorder):
    used[x] = 1
    for i in range(len(adj[x])):
        if used[adj[x][i]] == 0:
            DFS(adj[x][i], adj, used, postorder)
    postorder.append(x)


def number_of_strongly_connected_components(adj, adj_R):
    used = [0 for _ in range(len(adj))]
    vis = [0 for _ in range(len(adj))]
    postorder = []
    res = []

    for v in range(len(adj)):
        if used[v] == 0:
            DFS(v, adj, used, postorder)

    while postorder:
        v = postorder.pop()
        if vis[v] == 0:
            DFS(v, adj_R, vis, [])
            res.append(v)
    return res


if __name__ == '__main__':
    #input = sys.stdin.read()
    data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_R = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_R[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, adj_R))
