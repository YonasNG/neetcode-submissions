class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Optimal

        L, length = 0, 0
        n = len(s)
        seen = {}

        for R in range(n):
            if s[R] in seen:
                L = max(seen[s[R]] + 1, L)
            
            seen[s[R]] = R
            length = max(length, (R - L + 1))
        
        return length