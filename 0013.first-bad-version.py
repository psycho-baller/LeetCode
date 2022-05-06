#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (high + low) // 2
            if isBadVersion(mid):
                if isBadVersion(mid - 1):
                    high = mid - 1
                else:
                    return mid
            else:
                low = mid + 1
# @lc code=end

