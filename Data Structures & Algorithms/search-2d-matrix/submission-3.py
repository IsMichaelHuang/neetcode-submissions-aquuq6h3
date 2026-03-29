class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        row, col = len(matrix), len(matrix[0])
        top, bot = 0, row - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        left, right = 0, col - 1
        while left <= right:
            mid = (left + right) // 2 
            if target == matrix[row][mid]:
                return True

            if target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return False 

        