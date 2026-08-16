class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        res, curSum = nums[0], 0

        for num in nums:
            curSum = max(num, curSum + num)
            res = max(res, curSum)
        return res

        # Time: O(n)
        # Space: O(1)