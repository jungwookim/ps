from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float("inf")
        max_profit = 0
        for price in prices:
            if buy_price > price:
                buy_price = price
            if price - buy_price > max_profit:
                max_profit = price - buy_price

        return max_profit
