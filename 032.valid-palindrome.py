#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strings = [string.lower() for string in s if string.isalnum()]
        left, right = 0, len(strings) - 1
        while left < right:
            if strings[left] == strings[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
# @lc code=end

