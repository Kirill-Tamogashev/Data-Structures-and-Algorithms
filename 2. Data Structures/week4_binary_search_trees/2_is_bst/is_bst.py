import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(key, left, right):
  if key == []:
    return True
  res = []
  idx = 0
  arr_aux = []
  while True:
    if idx != -1:
      #print(key[idx], key[left[idx]])
      if key[idx] == key[left[idx]] and left[idx] > 0:
        return False
      arr_aux.append(idx)
      idx = left[idx]
    elif arr_aux:
      idx = arr_aux.pop()
      res.append(key[idx])
      idx = right[idx]
    else:
      break

  if res == sorted(res):
    return True
  return False


def main():
  nodes = int(sys.stdin.readline().strip())
  key = [0 for i in range(nodes)]
  left = [0 for i in range(nodes)]
  right = [0 for i in range(nodes)]
  for i in range(nodes):
   [a, b, c] = map(int, sys.stdin.readline().split())
   key[i] = a
   left[i] = b
   right[i] = c
  #print('key:   ',key)
  #print('left:  ', left)
  #print('right: ', right)

  if IsBinarySearchTree(key, left, right):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
