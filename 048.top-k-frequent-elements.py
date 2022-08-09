#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from collections import Counter
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        answer = []
        bucket_sort = [[] for _ in range(len(nums) + 1)]
        for num, count in counter.items():
            bucket_sort[count].append(num)
        while k > 0:
            popped = bucket_sort.pop()
            while popped:
                answer.append(popped.pop())
                k-= 1
        return answer
# @lc code=end

