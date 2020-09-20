def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def fast_sliding_window(sequence, n, m): 
    max_upto=[0 for i in range(n)] 
  
    max_elem_idx=[] 
    max_elem_idx.append(0) 
  
    for i in range(1,n): 
        while (len(max_elem_idx) > 0 and sequence[max_elem_idx[-1]] < sequence[i]): 
            max_upto[max_elem_idx[-1]] = i - 1
            del max_elem_idx[-1]           
        max_elem_idx.append(i)

    while (len(max_elem_idx) > 0): 
        max_upto[max_elem_idx[-1]] = n - 1
        del max_elem_idx[-1]
    

    answer = []
    j = 0
    for i in range(n - m + 1):  
        while (j < i or max_upto[j] < i + m - 1): 
            j += 1
        answer.append(sequence[j]) 
    return answer

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    m = int(input())
    print(*fast_sliding_window(input_sequence, n, m))

