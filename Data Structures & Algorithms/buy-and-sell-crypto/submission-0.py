class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        p = 0

        for price in prices:
            if price < b:
                b = price

            if price - b > p:
                p = price - b

        return p