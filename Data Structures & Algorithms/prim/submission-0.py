class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        # Adjacency List
        adj = collections.defaultdict(list)

        for n1, n2, weight in edges:
            adj[n1].append([n2, weight])
            adj[n2].append([n1, weight])
        
        # [vertex, weight]
        minHeap = [[0,0]]
        output = 0
        visit = set()

        while minHeap:
            weight, v = heapq.heappop(minHeap)
            if v in visit:
                continue
            output += weight
            visit.add(v)

            for neighbor, w in adj[v]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [w, neighbor])

        return output if len(visit) == n else -1
