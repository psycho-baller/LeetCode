from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # solution 1
        # max_wealth = 0
        # for account in accounts:
        #     wealth = sum(account)
        #     if wealth > max_wealth:
        #         max_wealth = wealth
        # return max_wealth

        # solution 2
        wealth = []
        for account in accounts:
            wealth.append(sum(account))
        return max(wealth)
