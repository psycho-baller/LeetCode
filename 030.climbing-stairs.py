#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n=2 -> 2
        # if n=3 -> 3
        # if n=4 -> 5
        # if n=5 -> 8
        # IT'S FIBONACCI SEQUENCE!
    #Dynamized:
        one, two = 1, 1
        for i in range(n):
            one, two = two, one + two
        return one


    # Memoized:
        # found_vals = {1: 1, 2: 2}
        # if n in found_vals.keys():
        #     return found_vals[n]
        # else:
        #     if n-1 in found_vals.keys():
        #         prev_seq = found_vals[n - 1]
        #     else:
        #         prev_seq = self.climbStairs(n-1)
        #         found_vals[n-1] = prev_seq
        #     if n-2 in found_vals.keys():
        #         prev_prev_seq = found_vals[n - 2]
        #     else:
        #         prev_prev_seq = self.climbStairs(n-2)
        #         found_vals[n-1] = prev_prev_seq
            
        #     next_sequence = prev_prev_seq + prev_seq
        #     found_vals[n] = next_sequence
        #     return next_sequence
            
# @lc code=end

