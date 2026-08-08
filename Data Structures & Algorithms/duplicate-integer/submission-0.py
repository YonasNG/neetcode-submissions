class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        return len(nums) > len(set(nums))

        # Time and Space: O(n)