class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        start, end = 0, 0

        for i in range(n):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > end - start:
                    start, end = l, r
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > end - start:
                    start, end = l, r
                l -= 1
                r += 1

        return s[start : end + 1]
