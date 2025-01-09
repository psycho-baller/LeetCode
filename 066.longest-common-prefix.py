#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word):
                    return strs[0][:i]
                if word[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


# @lc code=end
