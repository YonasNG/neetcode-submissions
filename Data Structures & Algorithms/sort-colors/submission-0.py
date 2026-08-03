class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        maxx = 3
        count = [0] * (maxx + 1)

        for x in nums:
            count[x] += 1
        
        i = 0
        for c in range(maxx + 1):
            while count[c] > 0:
                nums[i] = c
                i += 1
                count[c] -= 1