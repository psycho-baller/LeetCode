#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#


# @lc code=start
from typing import List, Literal


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        coord_to_dest = {}
        ends_in_both_oceans = []

        def in_the_shore_of(r, c) -> Literal["p", "a", "b"]:
            print("in_the_shore_of:", r, c)
            is_in_atlantic = (r == len(heights) - 1 and 0 <= c < len(heights[0])) or (
                c == len(heights[0]) - 1 and 0 <= r < len(heights)
            )
            is_in_pacific = (r == 0 and 0 <= c < len(heights[0])) or (
                c == 0 and 0 <= r < len(heights)
            )
            print("is_in_atlantic:", is_in_atlantic)
            print("is_in_pacific:", is_in_pacific)
            if is_in_atlantic and is_in_pacific:
                return "b"
            elif is_in_atlantic:
                return "a"
            elif is_in_pacific:
                return "p"
            else:
                return None

        def dfs(r, c, shores):
            # base case: if in the shore or all the neighbors are higher
            print("dfs:", r, c)

            if "b" in shores_it_reaches or (
                "a" in shores_it_reaches and "p" in shores_it_reaches
            ):
                return

            # if already visited
            if (r, c) in coord_to_dest:
                shores.append(coord_to_dest[(r, c)])
                return

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if not (0 <= new_r < len(heights) and 0 <= new_c < len(heights[0])):
                    continue
                if heights[r][c] >= heights[new_r][new_c]:
                    dfs(new_r, new_c, shores)
            shore = in_the_shore_of(r, c)
            if shore:
                coord_to_dest[(r, c)] = shore
                shores.append(shore)
                return

        if not heights:
            return []

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                print("____________________")
                print("r, c:", r, c)
                shores_it_reaches = []
                dfs(r, c, shores_it_reaches)
                print("shores_it_reaches:", shores_it_reaches)
                if "b" in shores_it_reaches or (
                    "a" in shores_it_reaches and "p" in shores_it_reaches
                ):
                    ends_in_both_oceans.append([r, c])
                coord_to_dest[(r, c)] = shores_it_reaches

        return ends_in_both_oceans


# @lc code=end
