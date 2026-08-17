class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        length, L, maxf = 0, 0, 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxf = max(count[s[R]], maxf)

            if R - L + 1 - maxf > k:
                count[s[L]] -= 1
                L += 1
            
            length = max(length, R - L + 1)
        
        return length