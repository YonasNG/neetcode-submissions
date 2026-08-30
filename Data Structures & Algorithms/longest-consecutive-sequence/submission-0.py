class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        res = 0

        for num in hashset:
            if (num - 1) not in hashset:

                length = 0
                while (num + length) in hashset:
                    length += 1
                    res = max(res, length)
        
        return res
