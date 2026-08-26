class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [[-1] * (M + 1) for _ in range(N)]
        return self.dfs(0, capacity, profit, weight, cache)

    def dfs(self, i, capacity, profit, weight, cache):
        if i == len(profit):
            return 0
            
        if cache[i][capacity] != -1:
            return cache[i][capacity]
            
        maxProfit = self.dfs(i + 1, capacity, profit, weight, cache)

        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfs(i, newCap, profit, weight, cache)
            maxProfit = max(p, maxProfit)

        cache[i][capacity] = maxProfit
        return maxProfit