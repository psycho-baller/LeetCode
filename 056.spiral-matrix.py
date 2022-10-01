#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        b, r = len(matrix), len(matrix[0])
        t, l = 0, 0
        
        while (r > l and t < b):
            
            
            for i in range(l,r):
                res.append(matrix[t][i])
            t+=1
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r-=1
            if (r <= l or t >= b):
                break
            for i in range(r-1, l-1,-1):
                res.append(matrix[b-1][i])
            b-=1
            for i in range(b-1, t-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res
        

sol = Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(sol)
# @lc code=end

