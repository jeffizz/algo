#!/usr/bin/env python3
from typing import List

prices = [7,1,5,3,6,4]
prices2 = [2,6,3,8,1,9,1,7]
prices3 = [4,7,1,2,11]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mpro,gmin,cmin,cmax = 0,0,0,0
        for index,price in enumerate(prices):
            if price >= prices[cmax]:
                if price - prices[cmin] > mpro:
                    cmax = index
                    cmin = gmin
                    mpro = price - prices[cmin]
            if gmin > cmin and (price - prices[gmin]) > mpro:
                cmin = gmin
                cmax = index
                mpro = price - prices[gmin]
            if price < prices[gmin]:
                gmin = index
        return mpro


    def maxProfit2(self, prices):
        # Initialize variables
        min_price = float('inf')  # Start with infinity
        max_profit = 0  # Start with no profit

        # Iterate through each price in the prices list
        for price in prices:
            # Update min_price if the current price is lower
            if price < min_price:
                min_price = price

            # Calculate the potential profit
            profit = price - min_price

            # Update max_profit if the current profit is greater
            if profit > max_profit:
                max_profit = profit

        return max_profit


result = Solution().maxProfit2(prices3)
print(result)
