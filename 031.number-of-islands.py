#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check_surroundings(r, c):
            grid[r][c] = "0"
            if r + 1 < len(grid) and grid[r + 1][c] == "1":
                check_surroundings(r + 1, c)
            if r - 1 >= 0 and grid[r - 1][c] == "1":
                check_surroundings(r - 1, c)
            if c + 1 < len(grid[0]) and grid[r][c + 1] == "1":
                check_surroundings(r, c + 1)
            if c - 1 >= 0 and grid[r][c - 1] == "1":
                check_surroundings(r, c - 1)

        islands = 0
        r, c = 0, 0
        while r < len(grid):
            while c < len(grid[0]):
                if grid[r][c] == "1":
                    islands += 1
                    check_surroundings(r, c)
                c += 1
            r += 1
            c = 0
        return islands


# @lc code=end


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = 0, 0
        islands = 0
        visited = set()

        def check_surroundings(r, c):
            if grid[r][c] == "1" and (r, c) not in visited:
                visited.add((r, c))
                if r + 1 < len(grid):
                    check_surroundings(r + 1, c)
                if r - 1 >= 0:
                    check_surroundings(r - 1, c)
                if c + 1 < len(grid[0]):
                    check_surroundings(r, c + 1)
                if c - 1 >= 0:
                    check_surroundings(r, c - 1)

        while r < len(grid):
            while c < len(grid[0]):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    check_surroundings(r, c)
                c += 1
            r += 1
            c = 0
        return islands
