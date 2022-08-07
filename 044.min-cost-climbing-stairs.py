#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = len(cost)-3
        first = cost[-1]
        second = cost[-2]
        while i >= 0:
            curr = cost[i] + min(first, second)
            first = second
            second = curr
            i -= 1
        return min(first, second)
# @lc code=end

