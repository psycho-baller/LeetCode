#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums)
        i = 0
        while i < end:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                end -= 1
            else:
                i += 1
# @lc code=end

    # or:
        # count = nums.count(0)
        # nums[:] = [i for i in nums if i != 0]
        # nums += [0]*count
