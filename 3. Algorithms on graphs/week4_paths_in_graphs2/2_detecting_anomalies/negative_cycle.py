import sys


def negative_cycle(adj, cost):
    #write your code here
    dist = [10000000000000] * len(adj)
    dist [0] = 0
    for j in range(len(adj)):
        for u in range(len(adj)):
            for v in adj[u]:
                idx = adj[u].index(v)
                if dist[v] > dist[u] + cost[u][idx]:
                    dist[v] = dist[u] + cost[u][idx]
                    if j == len(adj) - 1:
                        return 1 
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    adj_R = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        adj_R[b - 1].append(a - 1)
        cost[a - 1].append(w)
    #print(adj, '\n', cost)

    print(negative_cycle(adj, cost))
