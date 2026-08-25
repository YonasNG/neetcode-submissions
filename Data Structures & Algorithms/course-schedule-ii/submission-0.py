class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Topological Sort

        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a) # b -> a
            inDegree[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            numCourses -= 1

            for neigh in graph[node]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    q.append(neigh)
        
        return res if numCourses == 0 else []










