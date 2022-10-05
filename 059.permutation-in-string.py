#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# from itertools import permutations
# @lc code=start
import string


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Hashmap solution
        if len(s1) > len(s2):
            return False
        
        s1_map = dict.fromkeys(string.ascii_lowercase, 0)
        s2_map = dict.fromkeys(string.ascii_lowercase, 0)
        
        for i in range(len(s1)):
            s1_i = s1[i]
            s2_i = s2[i]
            s1_map[s1_i] += 1
            s2_map[s2_i] += 1

        for i in range(len(s1),len(s2)):
            if s1_map == s2_map:
                return True
            i_to_remove = s2[i-len(s1)]
            i_to_add = s2[i]
            s2_map[i_to_remove] = s2_map.get(i_to_remove, 0) - 1
            s2_map[i_to_add] = s2_map.get(i_to_add, 0) + 1

        return s1_map == s2_map
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


sol = Solution().checkInclusion(
    "ab",
    "eidbaooo")
print(sol)
# @lc code=end
