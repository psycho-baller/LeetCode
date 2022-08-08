#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = []
        anagrams = []
        strings = {}
        for s in strs:
            strings[s] = {}
            for c in s:
                strings[s][c] = strings[s].get(c,0) + 1
        while strs:
            first = strs[0]
            anagram = [first]
            del strs[0]
            for s in reversed(strs):
                if strings[first] == strings[s]:
                    anagram.append(s)
                    strs.remove(s)
            anagrams.append(anagram)
        return anagrams
# @lc code=end

