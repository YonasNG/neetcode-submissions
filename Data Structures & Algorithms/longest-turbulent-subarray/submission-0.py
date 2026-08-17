class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        up, down, max_len = 1, 1, 1
        n = len(arr)

        for i in range(1, n):
            if arr[i-1] > arr[i]:
                down = up + 1
                up = 1
            elif arr[i-1] < arr[i]:
                up = down + 1
                down = 1
            else:
                up = 1
                down = 1
            
            max_len = max(max_len, up, down)
        
        return max_len