class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Topological sort

        g = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            g[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        while q:
            node = q.popleft()
            numCourses -= 1
            for nei in g[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return numCourses == 0