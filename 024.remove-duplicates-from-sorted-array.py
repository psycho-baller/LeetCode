#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 0
        i = 1
        nums_len = len(nums)
        while (i + duplicates) < nums_len:
            if nums[i] == nums[i - 1]:
                nums.append(nums.pop(i))
                duplicates+=1
            else:
                i+=1
        non_duplicates = nums_len - duplicates
        return non_duplicates


# @lc code=end

