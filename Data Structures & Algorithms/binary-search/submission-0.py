class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        N, L = len(nums), 0 
        R = N - 1

        while L <= R:
            M = L + ((R - L ) // 2)
            if nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M - 1
            else:
                return M
        return -1