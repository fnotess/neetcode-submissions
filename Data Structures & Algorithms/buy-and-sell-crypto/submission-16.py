class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit=0
        buy_date = 0
        buy_price = prices[0]
    
        for i in range(len(prices)):
            today_price = prices[i]

            profit =  today_price- buy_price

            max_profit = max(profit,max_profit)
            
            buy_price = min(buy_price,today_price)

        return max_profit
        