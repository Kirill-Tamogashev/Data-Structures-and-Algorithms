# python3
class MaxMatching:
    def read_data(self):
        n, _ = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def BFS(self, n, m, adj_matrix):

        queue = [(1, None)]
        vis = set()
        vis.add((1, None))
        path = []
        parent = {}
        while queue:
            node = queue.pop(0)
            if node[0] == 1:
                for i in range(n):
                    if self.matching[i] == -1:
                        vis.add((2, i))
                        parent[(2, i)] = (1, None)
                        queue.append((2, i))
            elif node[0] == 2:
                i = node[1]
                for j in range(m):
                    if adj_matrix[i][j] == 1 and self.matching[i] != j and (3, j) not in vis:
                        vis.add((3, j))
                        parent[(3, j)] = node
                        queue.append((3, j))
            elif node[0] == 3:
                i = node[1]
                if not self.busy_right[i]:
                    prev = node
                    node = (4, i)
                    while True:
                        path.insert(0, (prev, node))
                        if prev[0] == 1: break
                        node = prev
                        prev = parent[node]
                    for edge in path:
                        if edge[0][0] == 2:
                            self.matching[edge[0][1]] = edge[1][1]
                        elif edge[0][0] == 3  and 4 == edge[1][0]:
                            self.busy_right[edge[1][1]] == True
                    return True
                else:
                    for j in range(n):
                        if self.matching[j] == i and (2, j) not in vis:
                            vis.add((2, j))
                            parent[(2, j)] = node
                            queue.append((2, j))
        return False


    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        self.matching = [-1] * n
        self.busy_right = [False] * m
        
        while self.BFS(n, m, adj_matrix):
            continue


        return self.matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
