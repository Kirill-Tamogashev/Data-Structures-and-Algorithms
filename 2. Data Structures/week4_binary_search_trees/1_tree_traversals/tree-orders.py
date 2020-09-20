# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    idx = 0
    arr = []
    while True:
      if idx != -1:
        arr.append(idx)
        idx = self.left[idx]
      elif arr:
        idx = arr.pop()
        self.result.append(self.key[idx])
        idx = self.right[idx]
      else:
        break
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    arr = []
    idx = 0
    while True:
      if idx != -1:
        self.result.append(self.key[idx])
        arr.append(idx)
        idx = self.left[idx]
      elif arr:
        idx = self.right[arr.pop()]
      else:
        break
    
    return self.result

  def postOrder(self):
    self.result = []
    arr = [0]
    while arr:
      idx = arr.pop()
      self.result.append(self.key[idx])

      left = self.left[idx]
      right = self.right[idx]
      if left != -1:
        arr.append(left)
      if right != -1:
        arr.append(right)

    return self.result[::-1]

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
