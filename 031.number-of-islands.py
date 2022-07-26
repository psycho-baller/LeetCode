#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check_surroundings(r, c, skip_row, skip_col):
            grid[r][c] = "0"
            rows_to_skip = skip_row + 1
            cols_to_skip = skip_col + 1
            if r+1 < len(grid) and grid[r+1][c] == "1":
                check_surroundings(r+1, c, rows_to_skip, cols_to_skip)
            if r-1 >= 0 and grid[r-1][c] == "1":
                check_surroundings(r-1, c, rows_to_skip, cols_to_skip)
            if c + 1 < len(grid[0]) and grid[r][c+1] == "1":
                check_surroundings(r, c+1, rows_to_skip, cols_to_skip)
            if c-1 >= 0 and grid[r][c-1] == "1":
                check_surroundings(r, c-1, rows_to_skip, cols_to_skip)

        islands = 0
        r, c = 0, 0
        while r < len(grid):
            while c < len(grid[0]):
                if grid[r][c] == "1":
                    islands += 1
                    check_surroundings(r, c, 0, 0)
                c+=1
            r+=1
            c=0
        return islands
# @lc code=end
