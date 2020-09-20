import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    vis = len(adj) * [0]

    distance[s] = 0
    reachable[s] = 1
    H = queue.Queue()

    for count in range(len(adj)):
        for u in range(len(adj)):
            for v in adj[u]:
                vidx = adj[u].index(v)
                if distance[u] != 10**19 and distance[v] > distance[u] + cost[u][vidx]:
                    distance[v] = distance[u] + cost[u][vidx]
                    reachable[v] = 1
                    if count == len(adj) - 1:
                        H.put(v)

    while not H.empty():
        u = H.get()
        vis[u] == 1
        if s != u: shortest[u] = 0
        for v in adj[u]:
            if vis[v] == 0:
                H.put(v)
                vis[v], shortest[v] = 1, 0
                
    distance[s] = 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

