class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x: int) -> int:
        # finds the root of x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        # Connects x and y
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            return True
        return False

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        minHeap = []
        for n1, n2, w in edges:
            heapq.heappush(minHeap, [w, n1, n2])
        
        unionfind = UnionFind(n)
        output, components = 0, n

        while components > 1 and minHeap:
            w, n1, n2 = heapq.heappop(minHeap)

            if unionfind.union(n1, n2):
                output += w
                components -= 1
        
        return output if components == 1 else -1
















