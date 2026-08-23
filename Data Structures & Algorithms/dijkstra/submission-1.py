class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        # Initialize the adjacency list for the nodes
        adj = {}
        for i in range(n):
            adj[i] = []
        
        # Populate the adjacency list with source, destination, and weight
        for s, d, w in edges:
            adj[s].append([d,w])
        
        # Initialize the dictionary and min-heap with src and a distance of 0
        shortest = {}
        minHeap = [[0, src]]
        
        while minHeap:
            
            # Pop the node with the minimum distance from the heap
            w1, n1 = heapq.heappop(minHeap)
            
            # Skip if we already found the shortest path to this node
            if n1 in shortest:
                continue
            shortest[n1] = w1

            # Loop through all neighbors of the current node
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest
