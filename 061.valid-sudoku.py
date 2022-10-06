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
                if b[r].isdigit() and b[r] in b[r+1:]:
                    return False
            # checks if the columns are valid
            col = [column[i] for column in board]
            for c in range(len(col)):
                if col[c].isdigit() and col[c] in col[c+1:]:
                    return False


        # check if all the boxes are valid
        for row in range(0, len(board), 3):
            for col in range(0, len(board[0]), 3):
                hSet = set()
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        val = board[r][c]
                        if val.isdigit():
                            if val in hSet:
                                return False
                            else:
                                hSet.add(val)

        return True
    
    
sol = Solution().isValidSudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
print(sol)
# @lc code=end
