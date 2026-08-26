class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Check if total sum is even or odd
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]
        # Time: O(n * target)
        # Space: O(target)