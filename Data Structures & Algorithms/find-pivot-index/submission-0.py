class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        totalsum = sum(nums)

        sumLeft = 0

        for i in range(len(nums)):
            sumRight = totalsum - sumLeft - nums[i]

            if sumRight == sumLeft:
                return i
            
            sumLeft += nums[i]
        
        return -1

        # Time: O(n)
        # Space: O(1)