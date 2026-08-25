class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        visit = set()
        res = 0
        minHeap = [(0,0)] # [(dist, v)]

        while len(visit) < n:
            d, v = heapq.heappop(minHeap)

            if v in visit:
                continue

            res += d
            visit.add(v)
            xi, yi = points[v]

            for j in range(n):
                if j not in visit:
                    xj, yj = points[j]
                    distance = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(minHeap, (distance, j))
                    
        return res
