#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i, letter in enumerate(strs[0]):
            prefix += letter
            for word in strs:
                if i >= len(word):
                    return prefix[:-1]
                if word[i] != prefix[-1]:
                    return prefix[:-1]
        return prefix


# @lc code=end
