class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        L, n, count = 1, len(nums), 1

        for i in range(1, n):

            if nums[i-1] == nums[i]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[L] = nums[i]
                L += 1
        
        return L
        