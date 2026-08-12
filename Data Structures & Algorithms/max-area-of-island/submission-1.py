class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if r == rows or c == cols or min(r, c) < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
        