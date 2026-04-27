class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fresh = 0

        # Find all rotten annanas
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        while q and fresh > 0:
            level = len(q)
            for _ in range(level):
                (r, c) = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        visit.add((row, col))
                        q.append((row, col)) 
            time += 1

        return time if not fresh else -1


        