class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        Current_Max = -1
        for i in range(len(arr) - 1, -1 , -1):
            new_max = max(arr[i], Current_Max)
            arr[i] = Current_Max
            Current_Max = new_max
        return arr
        