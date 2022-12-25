class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        future_max = 0
        max_profit = 0
        for _ in range(len(prices)):
            last_price = prices.pop()
            if last_price > future_max:
                future_max = last_price
            profit = future_max - last_price
            if profit > max_profit:
                max_profit = profit
        return max_profit