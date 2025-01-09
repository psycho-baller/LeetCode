#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#


# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 1
        count = 1
        current_letter_idx = 0
        current_letter = chars[current_letter_idx]
        while idx < len(chars):
            if chars[idx] == current_letter:
                count += 1
                if idx != len(chars) - 1:
                    idx += 1
                    continue
                if count > 1:
                    chars[current_letter_idx + 1 : idx + 1] = list(str(count))
                break
            print(
                "current_letter",
                current_letter,
                "count",
                count,
                "idx",
                idx,
                "current_letter_idx",
                current_letter_idx,
            )
            print("old chars", chars)
            # loop through current_letter_idx+1 -> idx and remove all the chars and replace with count
            if count > 1:
                chars[current_letter_idx + 1 : idx] = list(str(count))
                current_letter_idx = idx - (count - 2)
                idx = current_letter_idx + 1
                count = 1
            else:
                current_letter_idx = idx
                len_list = len(chars)
                idx += 1
            current_letter = chars[current_letter_idx]
            print("chars", chars)
        return len(chars)


# @lc code=end
