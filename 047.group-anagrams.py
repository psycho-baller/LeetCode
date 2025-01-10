#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            # count = [0] * 26
            # for c in s:
            #     key = ord(c) - ord("a")
            #     count[key] += 1
            counter = Counter(s)
            res[tuple(counter.items())].append(s)
        return list(res.values())

        # anagram = []
        # anagrams = []
        # strings = {}
        # for s in strs:
        #     strings[s] = {}
        #     for c in s:
        #         strings[s][c] = strings[s].get(c,0) + 1
        # while strs:
        #     first = strs[0]
        #     anagram = [first]
        #     del strs[0]
        #     for s in reversed(strs):
        #         if strings[first] == strings[s]:
        #             anagram.append(s)
        #             strs.remove(s)
        #     anagrams.append(anagram)
        # return anagrams


# @lc code=end
