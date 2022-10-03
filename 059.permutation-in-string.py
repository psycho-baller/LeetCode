#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# from itertools import permutations
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Hashmap solution
        
        
        
        # Time inefficient
        # s2_len = len(s2)
        # s1_len = len(s1)
        # i = s1_len
        
        # if s1_len > s2_len:
        #     return False
        
        # perm_s1 = [''.join(p) for p in permutations(s1)]

        # while i <= s2_len:
        #     if s2[i-s1_len:i] in perm_s1:
        #         return True
        #     i+=1

        # return False


sol = Solution().checkInclusion("adc", "dcda")
print(sol)
# @lc code=end
