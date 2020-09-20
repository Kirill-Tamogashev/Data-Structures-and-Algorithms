import sys

def bipartite(adj):
    #write your code here
    parity = len(adj) * [-1]
    while -1 in parity:
        s = parity.index(-1)
        parity[s] = 1
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v in adj[u]:
                if parity[v] == -1:
                    parity[v] = 1 - parity[u]
                    queue.append(v)
                elif parity[v] == parity[u]:
                    return 0         
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
