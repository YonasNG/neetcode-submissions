class Solution:
    def climbStairs(self, n: int) -> int:

        # 1D-DP Bottom Up Constant Space Approach
        if n <= 2:
            return n
        
        prev = 1
        cur = 2

        for i in range(2, n):
            prev, cur = cur, prev + cur
        
        return cur


        # 1D-DP Top-Down Memorization Approach
        memo = {1:1, 2:2}

        def fib(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = fib(n-2) + fib(n-1)
                return memo[n]
        
        return fib(n)
        