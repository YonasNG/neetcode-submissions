class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        empty, fresh, rotten = 0, 1, 2
        queue = deque()
        fresh_num = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == rotten:
                    queue.append((i,j))
                elif grid[i][j] == fresh:
                    fresh_num += 1
        time = 0
        while fresh_num > 0 and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == fresh:
                        grid[nr][nc] = rotten
                        queue.append((nr, nc))
                        fresh_num -= 1
            time += 1
        
        return time if fresh_num == 0 else -1
            
