#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current_letter_idx = 0
        prefix = ""
        while True:
            prefix += strs[0][current_letter_idx]
            for word in strs:
                if current_letter_idx >= len(word):
                    return prefix[:-1]
                if word[current_letter_idx] != prefix[-1]:
                    return prefix[:-1]
            current_letter_idx += 1
        return prefix


# @lc code=end
