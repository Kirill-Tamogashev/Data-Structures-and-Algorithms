# python3
from sys import stdin


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def SelectPivotElement(a, used_rows, used_columns):
    size = len(a)

    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    while 0 == a[pivot_element.row][pivot_element.column]:
        pivot_element.column +=1
        if pivot_element.row > size - 1:
          return None
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column

def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    row_size = len(a)
    column_size = len(a[0])

    mult = a[pivot_element.row][pivot_element.column]

    for i in range(column_size):
        a[pivot_element.row][i] = a[pivot_element.row][i] / mult
    b[pivot_element.row] = b[pivot_element.row] / mult

    for i in range(row_size):
        if i != pivot_element.row:
            mult = a[i][pivot_element.column]
            for j in range(pivot_element.column, row_size):
                a[i][j] -= a[pivot_element.row][j] * mult
            b[i] -= b[pivot_element.row] * mult


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for _ in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b

def append_constraints(n, mA, b):
  for _ in range(m):
    A.append([-1.0] * m)
    b.append(0.0)
  A.append([1.0] * m)
  b.append(10**9)
  return A, b


  
def solve_diet_problem(n, m, A, b, c):  
  # Write your code here





  return [0, [0] * m]

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

anst, ansx = solve_diet_problem(n, m, A, b, c)

if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")
    
