# https://leetcode.com/problems/two-sum/
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# Notion: https://www.notion.so/rami-m/leetcode-course-e4229bacae0240e194a02cc0685959b3?p=174f55603e85805c8975e738a9c7845b&pm=s

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Sorting & Binary Search
        # A = []
        # for i, num in enumerate(nums):
        #     A.append((num, i))
        # A.sort()

        # i, j = 0, len(A) - 1
        # while i < j:
        #     if A[i][0] + A[j][0] == target:
        #         return [A[i][1], A[j][1]]
        #     elif A[i][0] + A[j][0] < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return []

        # One-pass Hash Table
        value_to_index = {}
        for i, num in enumerate(nums):
            if target - num in index_to_value:
                return [index_value[target - num], i]
            index_to_value[num] = i

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
