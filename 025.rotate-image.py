#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)
        for x in range(length//2):
            for y in range(x, length-x-1):
                # swap w right
                matrix[x][y], matrix[y][length -
                                        x-1] = matrix[y][length-x-1], matrix[x][y]
                # swap w corner
                matrix[x][y], matrix[length-x-1][length -
                                                  y-1] = matrix[length-x-1][length-y-1], matrix[x][y]

                # swap w bottom
                matrix[x][y], matrix[length-y -1][x] = matrix[length-y-1][x], matrix[x][y]



                
                

# using dummy matrix:
        # dummy_matrix = [array[:] for array in matrix]
        # length = length = len(matrix)
        # for x in range(length):
        #     for y in range(length):
        #         matrix[x][y] = dummy_matrix[length-y-1][x]
# @lc code=end

