from collections import defaultdict

def tree_height(tree, root):
    q = []

    q.append(root)
    q.append("$")

    height = 1

    while q != []:
        elem = q.pop(0)
        if elem == "$" and q != []:
            elem = q.pop(0)
            height += 1
            q.append("$")
        
        for child in tree[elem]:
            q.append(child)
        
    return height


n = int(input())
parents = list(map(int, input().split()))

tree = defaultdict(list)

for node,parent in enumerate(parents):
    tree[parent].append(node)
root = tree.pop(-1)[0]
print(tree_height(tree, root))
