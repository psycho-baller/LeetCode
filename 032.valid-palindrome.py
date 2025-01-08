#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:

    def isPalindrome(self, s: str) -> bool:
        # O(n) time and O(1) space
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
        return True

    # def isPalindrome(self, s: str) -> bool:
    #     # O(n) time and O(n) space
    #     strings = [string.lower() for string in s if string.isalnum()]
    #     left, right = 0, len(strings) - 1
    #     while left < right:
    #         if strings[left] == strings[right]:
    #             left += 1
    #             right -= 1
    #         else:
    #             return False
    #     return True


# @lc code=end
