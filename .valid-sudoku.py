#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):

            # checks if the rows are valid
            for r in range(len(board[i])):
                b = board[i]
                print(b[r], b[r+1:])
                if b[r].isdigit() and b[r] in b[r+1:]:
                    return False
            # checks if the columns are valid
            col = [column[i] for column in board]
            for c in range(len(col)):
                print(col[c], col[c+1:])
                if col[c].isdigit() and col[c] in col[c+1:]:
                    return False
            # check if the boxes are valid in the row dir
            
            # check if the boxes are valid in the col dir
            
            # check if the boxes are valid in the diag dir
            
        

        return True
    
    
sol = Solution().isValidSudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
print(sol)
# @lc code=end
