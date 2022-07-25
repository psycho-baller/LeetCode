#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = defaultdict(int)
        dic_t = defaultdict(int)
        len_list = len(s)
        if len_list != len(t):
            return False
        for i in range(len_list):
            char_s = s[i]
            char_t = t[i]
            dic_s[char_s] += dic_s[char_s] + 1
            dic_t[char_t] += dic_t[char_t] + 1
        print(dic_s, dic_t, s, t)
        if dic_s == dic_t:
            return True
        else:
            return False

sltn = Solution()
print(sltn.isAnagram("rat","tar"))
# @lc code=end

