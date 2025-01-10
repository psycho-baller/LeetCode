#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#


# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            grouped_letters = 1
            while (
                i + grouped_letters < len(chars)
                and chars[i] == chars[i + grouped_letters]
            ):
                grouped_letters += 1
            chars[res] = chars[i]
            res += 1
            if grouped_letters > 1:
                str_repr = str(grouped_letters)
                chars[res : res + len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += grouped_letters
        return res

        # idx = 0
        # res = 0
        # while idx < len(chars):
        #     count = 1
        #     while idx + count < len(chars) and chars[idx + count] == chars[idx]:
        #         count += 1
        #     chars[res] = chars[idx]
        #     res += 1
        #     if count > 1:
        #         str_rep = str(count)
        #         chars[res : res + len(str_rep)] = list(str_rep)
        #         res += len(str_rep)
        #     idx += count
        # return res


# @lc code=end
