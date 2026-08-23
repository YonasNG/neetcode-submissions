class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res, curr = [], []

        def backtrack(i):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for j in range(i, n + 1):
                curr.append(j)
                backtrack(j + 1)
                curr.pop()
        
        backtrack(1)
        return res