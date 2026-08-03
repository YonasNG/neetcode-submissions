# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        n = len(pairs)
        if n <= 1:
            return pairs

        m = n // 2
        Left = self.mergeSort(pairs[:m])
        Right = self.mergeSort(pairs[m:])

        l, r, i = 0, 0, 0

        sorted_arr = [0] * n

        while l < len(Left) and r < len(Right):
            if Left[l].key <= Right[r].key:
                sorted_arr[i] = Left[l]
                l += 1
            else:
                sorted_arr[i] = Right[r]
                r += 1
            i += 1

        while l < len(Left):
            sorted_arr[i] = Left[l]
            l += 1
            i += 1
        
        while r < len(Right):
            sorted_arr[i] = Right[r]
            r += 1
            i += 1

        return sorted_arr
        
