from typing import List
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dict = defaultdict(int)
        for list in nums:
            for num in list:
                dict[num] += 1
        exists_in_all = []
        for key, value in dict.items():
            if value == len(nums):
                exists_in_all.append(key)
        exists_in_all.sort()
        return exists_in_all


print(Solution().intersection([[12,2,5],[12,4,5,6],[12,5,8,9]]))
