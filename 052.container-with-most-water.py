#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        cur_max = 0
        while right > left:
            width = right - left
            length = min(height[left], height[right])
            area = width * length
            cur_max = max(cur_max, area)
            if height[left] < height[right]:
                move_right = 1
                while left + move_right < right and height[left] > height[left + move_right]:
                    move_right+=1
                left = left + move_right
            else:
                move_left = 1
                while right - move_left > left and height[right] > height[right - move_left]:
                    move_left+=1
                right = right - move_left
        return cur_max
# @lc code=end

