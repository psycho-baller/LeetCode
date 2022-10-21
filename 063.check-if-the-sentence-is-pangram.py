#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        words = [0]*26
        sentence = list(sentence)
        for char in sentence:
            asc = ord(char)
            index = asc - ord('a')
            words[index] = 1
        return 0 not in words
# @lc code=end

