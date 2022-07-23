#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from ast import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        answer = nums[0]
        for i in range(1,len(nums)):
            curr_num = nums[i]
            if curr_num == answer:
                count += 1
            elif count == 0:
                answer = curr_num
            else:
                count-=1
        return answer



        # d = defaultdict(int)
        # for num in nums:
        #     d[num] = d[num] + 1
        # for (k,v) in d[1]:
        #     if v > (len(nums))/2:
        #         return k
# @lc code=end

