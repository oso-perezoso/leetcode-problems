# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price: int = prices[0]
        max_profit: int = 0

        for pr in prices[1:]:
            lowest_price = min(lowest_price, pr)
            max_profit = max(max_profit, pr - lowest_price)

        return max_profit
