class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == 'O':
                board[r][c] = 'T'

                capture(r + 1, c)
                capture(r - 1, c)
                capture(r, c + 1)
                capture(r, c - 1)

        # Capture the O's around boarder
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS - 1] or c in [0, COLS - 1] and board[r][c] == 'O':
                    capture(r, c)

        # Capture the O's within board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                
        # Uncapture the O's around boarder
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                
        