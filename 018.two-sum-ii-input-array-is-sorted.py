#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        # def condition(num, mid) -> bool:
        #     if num + numbers[mid] > target:
        #         return True
        #     return False

        # # for num in numbers:
        # for i in range(len(numbers)):
        #     left, right = i+1, len(numbers)
        #     while left < right:
        #         mid = left + (right - left) // 2
        #         if condition(numbers[i], mid):
        #             right = mid
        #         else:
        #             left = mid + 1
        #     if numbers[i] + numbers[left - 1] == target:
        #         return [i+1, left]


# @lc code=end
