class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            pay_out = prices[i] - buy_price
            if pay_out < 0:
                buy_price = prices[i]
            elif pay_out > max_profit:
                max_profit = pay_out
        return max_profit
        