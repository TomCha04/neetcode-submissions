class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 # default value if no profit can be made
        min_buying_price = prices[0] # Initialize as the 1st possible buying price
        
        for price in prices:
            # profit for current price = price - min_buying_price
            max_profit = max(max_profit, price - min_buying_price)
            min_buying_price = min(min_buying_price, price)
        return max_profit