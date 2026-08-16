class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        globMax, globMin = nums[0], nums[0]
        curMax, curMin, total = 0, 0, 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)

            globMax = max(curMax, globMax)
            globMin = min(curMin, globMin)

            total += n
        
        return max(total - globMin, globMax) if globMax > 0 else globMax

        # Time: O(n)
        # Space: O(1)