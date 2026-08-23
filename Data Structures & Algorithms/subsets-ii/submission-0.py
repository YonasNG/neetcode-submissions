class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)

        res, subset = [], []

        def backtrack(i):
            if i == n:
                res.append(subset[:])
                return
            
            # Include nums[i]
            subset.append(nums[i])
            backtrack(i+1)

            # Don't include nums[i]
            subset.pop()

            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1)
        
        backtrack(0)
        return res
        