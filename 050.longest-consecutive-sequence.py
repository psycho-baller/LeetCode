#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0
        for num in numSet:
            counter = 0
            if (num -1) not in numSet:
                counter+=1
                tmp = num
                while (tmp + counter) in numSet:
                    counter+=1
                maxCount = max(counter, maxCount)
        return maxCount
            
# @lc code=end

