class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        n, m = len(profit), capacity

        cache = [[-1] * (m+1) for _ in range(n)]
        return self.dfs(0, capacity, profit, weight, cache)
    
    def dfs(self, i, capacity, profit, weight, cache):
        if i == len(profit):
            return 0
        
        if cache[i][capacity] != -1:
            return cache[i][capacity]
        
        # Skip i
        maxProfit = self.dfs(i+1, capacity, profit, weight, cache)

        # Include i
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfs(i+1, newCap, profit, weight, cache)
            maxProfit = max(maxProfit, p)
        cache[i][capacity] = maxProfit
        return maxProfit