# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        n = len(pairs)
        # Edge Case
        if len(pairs) <= 1:
            return pairs
        
        # Pivot and left pointer
        pivot = pairs[-1]
        left = 0

        # Iterate through the array
        for i in range(n - 1):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1

        pairs[left], pairs[-1] = pairs[-1], pairs[left]

        # Quick sort left and right side
        L = self.quickSort(pairs[:left])
        R = self.quickSort(pairs[left + 1:])

        return L + [pivot] + R
