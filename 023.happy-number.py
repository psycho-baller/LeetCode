#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def getSum(self, n):
        # num = [int(i) for i in list(str(n).split())]
        # summ = 0
        # for i in num:
        #     summ += (i**2)
        # return sum
        summ = 0
        output = n
        while output != 0:
            temp_unit = output%10
            temp_unit = temp_unit**2

            summ += temp_unit
            output = output//10
        return summ

    def isHappy(self, n: int) -> bool:
        sltn = n
        sums = set()
        while sltn not in sums:
            sums.add(sltn)
            sltn = self.getSum(sltn)
        if sltn != 1:
            return False
        return True
# @lc code=end

