#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        len_nums = len(nums)

        for i in range(len_nums):
            # if the current number is the same as the previous number, skip it
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # two pointers
            left, right = i + 1, len_nums - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res

        # len_nums = len(nums)
        # ans = []
        # nums.sort()

        # for i,v in enumerate(nums):
        #     if i>0 and v == nums[i - 1]:
        #         continue
        #     left, right = i + 1, len_nums -1
        #     while right > left:
        #         if v + nums[left] + nums[right] > 0:
        #             right-=1
        #         elif v + nums[left] + nums[right] < 0:
        #             left += 1
        #         else:
        #             ans.append([v, nums[left], nums[right]])
        #             left+=1
        #             while nums[left] == nums[left-1] and left < right:
        #                 left+=1
        # return ans # O(n^2) time | O(n,1) space

        # O(n^3) time | O(n,1) space
        # one = 0
        # while one < len_nums-2:
        #     two = one + 1
        #     while two < len_nums-1:
        #         if nums[one] + nums[two] + nums[-1] >= 0:
        #             three = two + 1
        #             while three < len_nums:
        #                 if nums[one] + nums[two] + nums[three] == 0 and [nums[one], nums[two], nums[three]] not in ans:
        #                     ans.append([nums[one], nums[two], nums[three]])
        #                 three+=1
        #         two+=1
        #     one+=1
        # return ans


# @lc code=end
