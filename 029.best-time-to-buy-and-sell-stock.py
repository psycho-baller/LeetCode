#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_diff = 0
        len_prices = len(prices)
        while r < len_prices:
            buy = prices[l]
            sell = prices[r]
            # if we see a time where its cheaper to buy,
            # we change the buying time to that pointer(right)
            # and move that pointer one index to the right
            if buy > sell:
                l = r
            else:
                max_diff = max(sell - buy, max_diff)
            r += 1

        return max_diff

# Failed attempt:
        # mini = min(prices)
        # index_of_min = prices.index(mini)
        # if mini == prices[-1]:
        #     return 0
        # maxi = max(prices[index_of_min+1:])
        # profit = maxi - mini
        # return profit
# @lc code=end
