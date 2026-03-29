class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqr = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur = board[r][c]

                # We only care about the integer value
                if cur == ".":
                    continue

                if (cur in rows[r] or
                    cur in cols[c] or
                    cur in sqr[(r // 3, c // 3)]):
                    return False
                
                # Update the HashSets
                rows[r].add(cur)
                cols[c].add(cur)
                sqr[(r // 3, c // 3)].add(cur)
        return True

        # Time: O(c) where c is the constant as there will always be 9x9 grid
        # Space: O(c) where c is the constant as there will always be 9x9 grid

