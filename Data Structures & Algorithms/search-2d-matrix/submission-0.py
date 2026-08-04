class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Get number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols

        # Set up pointers for binary search
        l, r = 0, total - 1

        # Perform binary search
        while l <= r:
            mid = l + (r - l) // 2

            # Convert 1D index mid back to 2D coordinates
            i = mid // cols
            j = mid % cols
            current_val = matrix[i][j]


            if current_val > target:
                r = mid - 1
            elif current_val < target:
                l = mid + 1
            else:
                return True

        return False
