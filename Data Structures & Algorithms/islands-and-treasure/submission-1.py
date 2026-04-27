class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit: set(tuple(int, int)) = set()
        q = deque()

        def layer(r, c):
            # Do work
            if (r, c) in visit or \
                r >= ROWS or c >= COLS or \
                r < 0 or c < 0 or \
                grid[r][c] == -1:
                return
            
            visit.add((r, c))
            q.append((r, c))

        # Find all teasure positions
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                (r, c) = q.popleft()
                grid[r][c] = dist

                layer(r + 1, c)
                layer(r - 1, c)
                layer(r, c + 1)
                layer(r, c - 1)

            dist += 1
                



        