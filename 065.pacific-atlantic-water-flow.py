#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#


# @lc code=start
from typing import List, Literal


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        top_edges = [(0, c) for c in range(len(heights[0]))]
        left_edges = [(r, 0) for r in range(len(heights))]
        bottom_edges = [(len(heights) - 1, c) for c in range(len(heights[0]))]
        right_edges = [(r, len(heights[0]) - 1) for r in range(len(heights))]
        pacific_edges = top_edges + left_edges
        atlantic_edges = bottom_edges + right_edges

        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return
            ocean.add((r, c))
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if (
                    0 <= new_r < len(heights)
                    and 0 <= new_c < len(heights[0])
                    and heights[new_r][new_c] >= heights[r][c]
                ):
                    dfs(new_r, new_c, ocean)

        pacific = set()
        atlantic = set()
        for r, c in pacific_edges:
            dfs(r, c, pacific)
        for r, c in atlantic_edges:
            dfs(r, c, atlantic)

        return list(pacific & atlantic)


# @lc code=end
