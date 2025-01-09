#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # remove duplicates
        idx = 1
        while idx < len(nums):
            if nums[idx - 1] == nums[idx]:
                nums.pop(idx)
                # duplicates += 1
            else:
                idx += 1
        return len(nums)

        # count duplicates then subtract it from it's length to find the len of unique
        # duplicates = 0
        # i = 1
        # nums_len = len(nums)
        # while (i + duplicates) < nums_len:
        #     if nums[i] == nums[i - 1]:
        #         nums.append(nums.pop(i))
        #         duplicates+=1
        #     else:
        #         i+=1
        # non_duplicates = nums_len - duplicates
        # return non_duplicates

        # two pointers
        # l = r = 0
        # while r < len(nums):
        #     nums[l] = nums[r]
        #     while nums[r] == nums[l] and r < len(nums):
        #         r += 1
        #     l += 1
        # return l


# @lc code=end
