class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        top_sort = []
        visited = set()
        visiting = set()


        def dfs(u):
            if u in visited:
                return True
            if u in visiting:
                return False
            
            visiting.add(u)

            for neighbor in adj[u]:
                if not dfs(neighbor):
                    return False
            visiting.remove(u)
            visited.add(u)
            top_sort.append(u)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
                
        top_sort.reverse()
        return top_sort