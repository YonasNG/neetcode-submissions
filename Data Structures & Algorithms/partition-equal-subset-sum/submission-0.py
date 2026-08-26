class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Check if total sum is even or odd
        total = sum(nums)
        if total % 2:
            return False
        
        dp = {0}
        target = total // 2

        for num in nums:
            nextDP = set(dp)
            for x in dp:
                if num + x == target:
                    return True
                
                if num + x < target:
                    nextDP.add(num + x)
            
            dp = nextDP
        
        return False
        
        # Time: O(n * target)
        # Space: O(target)