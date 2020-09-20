import numpy as np 


c = [1, 2, 3]
A = [[1, 2], [3, 2], [5, 4]]
b = [3, 5, 3]

res = np.linprog(-np.array(c), A, b)
print(res)