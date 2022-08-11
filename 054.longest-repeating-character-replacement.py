#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        max_f = 0
        l = 0
        char_to_amount = {}
        for r in range(len(s)):
            char_to_amount[s[r]] = 1 + char_to_amount.get(s[r],0)
            max_f = max(max_f, char_to_amount[s[r]])

            while r-l+1 - max_f > k:
                char_to_amount[s[l]] -= 1
                l += 1

            max_count = max(r - l + 1, max_count)

        return max_count

# @lc code=end

