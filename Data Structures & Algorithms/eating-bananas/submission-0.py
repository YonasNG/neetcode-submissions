class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Define a function to check whether the value of k works
        def k_works(k):
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/k)

            return hour <= h
        
        l = 1
        r = max(piles)

        # Do binary search (conditional) on the possible values of k
        while l < r:
            mid = l + ((r - l) // 2)
            if k_works(mid):
                r = mid
            else:
                l = mid + 1

        return r

    # Time Complexity: O(log(max(piles)) * n)
    # Space Complexity: O(1)    

    