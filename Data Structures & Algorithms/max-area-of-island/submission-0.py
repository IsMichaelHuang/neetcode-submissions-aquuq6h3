class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def dfs(r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == 0:
                return 0 

            grid[r][c] = 0
            r_sum = 1
            r_sum += dfs(r - 1, c)
            r_sum += dfs(r + 1, c)
            r_sum += dfs(r, c + 1)
            r_sum += dfs(r, c - 1)
            return r_sum



        # Find the point of entry
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        return area
        