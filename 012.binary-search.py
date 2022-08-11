#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        while len(nums) > 1:
            mid = int(len(nums) / 2)
            if nums[mid] == target:
                return mid + count
            if nums[mid] > target:
                nums = nums[:mid]
            else:
                count+=mid
                nums = nums[mid:]
        return -1 if nums[0] != target else 0
# @lc code=end

