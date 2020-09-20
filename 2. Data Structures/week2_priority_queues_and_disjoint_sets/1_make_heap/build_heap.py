def relative(i, name):
    if name == 'Parent':
        return int((i - 1)/ 2)
    elif name == 'leftchild':
        return (i + 1) * 2 - 1
    elif name == 'rightchild':
        return (i + 1) * 2

def SiftUp(i, H):
    swaps = []
    p = relative(i, 'Parent')
    while i > 0 and H[p] < H[i]:
        H[p], H[i] =  H[i], H[p]
        swaps.append(i, p)
        i = p
    return swaps

def SiftDown(i, H, size):
    max_idx = i
    swaps = []
    
    l = relative(i, 'leftchild')
    if l <= size and H[l] < H[max_idx]:
        max_idx = l

    r = relative(i, 'rightchild')
    if r <= size and H[r] < H[max_idx]:
        max_idx = r

    if i != max_idx:
        H[i], H[max_idx] = H[max_idx], H[i]
        swaps.append((i, max_idx))
        swaps += SiftDown(max_idx, H, size)
    return swaps


def build_heap(data, n):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    size = n - 1
    i = size // 2
    while i >= 0:
        swap = SiftDown(i, data, size)
        if swap != []:
            swaps += swap
        i -= 1
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data, n)

    print(len(swaps))
    for i in swaps:
        print(*i)
    #print(swaps)
    #print(data)


if __name__ == "__main__":
    main()
