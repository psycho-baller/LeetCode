#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        one_d_matrix = []
        left, right = 0, len(matrix)
        len_mat = len(matrix[0])
        # first bs
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target <= matrix[mid][len_mat -1]:
                one_d_matrix = matrix[mid]
                print(one_d_matrix)
                l, r = 0, len(one_d_matrix)
                # Second bs
                while l < r:
                    mid = l + (r - l) // 2
                    if one_d_matrix[mid] > target:
                        r = mid
                    elif one_d_matrix[mid] < target:
                        l = mid + 1
                    else:
                        return True
                return False
            elif target < matrix[mid][0]:
                right = mid
            else:
                left = mid + 1
        return False


sol = Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
    3)
print(sol)
# @lc code=end

