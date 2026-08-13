class Solution:
    def rob(self, nums: List[int]) -> int:

        # DP - Constant Space Approach
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2
        
        
        # Bottom Up DP (Tabulation)
        n = len(nums)

        if n == 1: 
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1]) 

        return dp[n-1]
        
        # Top Down DP (Memorization)
        n = len(nums)
        memo = {0: nums[0], 1: max(nums[0], nums[1])}
        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(helper(i-1), helper(i-2) + nums[i])
                return memo[i]
        
        helper(n-1)
        
        # Recursive
        def recursive(i):
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0], nums[1])
            
            return max(recursive(i-1), recursive(i-2) + nums[i])  

        return recursive(len(nums) - 1)      