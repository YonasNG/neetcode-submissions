class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res, subset = [], []

        def backtrack(i):
            if i == n:
                res.append(subset[:])
                return
            
            # Pick nums[i]
            subset.append(nums[i])
            backtrack(i+1)

            # Don't pick nums[i]
            subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res