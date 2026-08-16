class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        window_sum = sum(arr[:k])
        count = 0
        n = len(arr)

        for L in range(n - k + 1):
            if window_sum >= threshold * k:
                count += 1
            
            if L + k < n:
                window_sum += arr[L + k]
                window_sum -= arr[L]
            
        return count

        # Time: O(n)
        # Space: O(1)