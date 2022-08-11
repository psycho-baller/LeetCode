# https://leetcode.com/problems/two-sum/
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



    #     unsorted_nums = nums
    #     nums = sorted(nums)
    #     l, r = 0, 1
    #     len_nums = len(nums)
    #     while l < len_nums and r < len_nums:
    #         val = nums[l] + nums[r]
    #         if val < target:
    #             r+=1
    #         elif val > target:
    #             r+=1
    #             l+=1
    #         else:
    #             for i in range(len_nums):
    #                 if unsorted_nums[i] == nums[l]:
    #                     left = i
    #                 if unsorted_nums[i] == nums[r]:
    #                     right = i
    #             return [left,right]
# @lc code=end
