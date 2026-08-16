class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L, total, n = 0, 0, len(nums)
        length = float("inf")

        for R in range(n):
            total += nums[R]

            while total >= target:
                length = min(length, R - L + 1)
                total -= nums[L]
                L += 1

        return length if length != float("inf") else 0

        # Time: O(n)
        # Space: O(1)

