class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res, ans = [], []

        def backtrack(i, curr):
            if curr == target:
                res.append(ans[:])
                return
            
            if curr > target or i == len(candidates):
                return
            
            # Include
            ans.append(candidates[i])
            backtrack(i, curr + candidates[i])
            ans.pop()

            # Exclude
            backtrack(i+1, curr)

        
        backtrack(0, 0)
        return res