class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        L, R = 0, n - 1
        res = [0] * n
        res_index = n - 1

        while L <= R:
            if abs(nums[L]) > abs(nums[R]):
                res[res_index] = (nums[L] ** 2)
                L += 1
            else:
                res[res_index] = (nums[R] ** 2)
                R -= 1

            res_index -= 1
        return res