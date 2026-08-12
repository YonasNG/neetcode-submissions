class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        original = image[sr][sc] # Original color

        if original == color:
            return image
        
        rows, cols = len(image), len(image[0])

        def fill(r, c):
            if min(r, c) < 0 or r == rows or c == cols or image[r][c] != original:
                return
            
            image[r][c] = color
            fill(r + 1, c)
            fill(r - 1, c)
            fill(r, c + 1)
            fill(r, c - 1)
        
        fill(sr, sc)
        return image

        # Time: O(N)
        # Space: O(N)