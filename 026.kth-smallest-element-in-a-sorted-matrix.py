#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def condition(mid, len_matrix) -> bool:
            count = 0
            col = len_matrix - 1
            row = 0
            while col >= 0 and row < len_matrix:
                ith_list = matrix[row][col]
                if ith_list <= mid:
                    count = count + col + 1
                    row+=1
                else:
                    col-= 1
            return count >= k


        len_matrix = len(matrix)
        left, right = matrix[0][0], matrix[len_matrix-1][len_matrix-1]
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid, len_matrix):
                right = mid
            else:
                left = mid + 1
        return left




    #    len_matrix = len(matrix)
    #    if len_matrix < 2:
    #     return matrix[k-1][k-1]
    #    index_k_is_in = k//len_matrix
    #    num_of_vals_skipped = index_k_is_in * len_matrix
    #    index_of_k = k - num_of_vals_skipped - 1
    #    return matrix[index_k_is_in][index_of_k]
# @lc code=end

