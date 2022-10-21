#
# @lc app=leetcode id=2299 lang=python3
#
# [2299] Strong Password Checker II
#

# @lc code=start
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        lower = False
        upper = False
        num = False
        special = False
        lenght = 0
        A = list(password)
        for i in range(len(A)):
            if A[i].islower():
                lower = True
            elif A[i].isupper():
                upper = True
            elif A[i].isdigit():
                num = True
            elif A[i] in ['$', '#', '@', '%', '&', '!', '*', "^", '+', '-', '(', ')']:
                special = True
            lenght += 1
            if i < len(A)-1 and A[i] == A[i+1]:
                return False
        return (lenght >= 8) and (lower and upper and num and special)
# @lc code=end

