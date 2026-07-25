class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = current = 0
        for num in nums:
            current = current + 1 if num else 0
            result = max(result,current)
        return result

        