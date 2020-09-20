def optimal_weight(W, w):
    # write your code here
    n = len(w)
    value = []
    for _ in range(W + 1):
        m = [0] * (n)
        value.append(m)
    for i in range(n):
        for j in range(1, W + 1):
            value[j][i] = value[j][i - 1]
            if w[i] <= j:
                val = value[j - w[i]][i - 1] + w[i]
                if val > value[j][i]:
                    value[j][i] = val
    return value[W][n - 1]


W, n = list(map(int, input().split()))
w = list(map(int, input().split()))
print(optimal_weight(W, w))