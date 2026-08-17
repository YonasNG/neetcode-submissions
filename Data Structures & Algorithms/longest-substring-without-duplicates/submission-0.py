class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Sliding Window Approach

        L, length = 0, 0
        n = len(s)
        window = set()

        for R in range(n):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            
            window.add(s[R])
            length = max(length, (R - L + 1))
        
        return length