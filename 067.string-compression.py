#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#


# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        res = 0
        while idx < len(chars):
            count = 1
            while idx + count < len(chars) and chars[idx + count] == chars[idx]:
                count += 1
            chars[res] = chars[idx]
            res += 1
            if count > 1:
                str_rep = str(count)
                chars[res : res + len(str_rep)] = list(str_rep)
                res += len(str_rep)
            idx += count
        return res


# @lc code=end
