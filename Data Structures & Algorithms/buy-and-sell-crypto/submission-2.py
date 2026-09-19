class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0 # default value if no profit can be made

        # ALL days BEFORE sell day are valid buy days
        for s in range(1, len(prices)): # 1st valid sell day = day 1
            # [1, 1]
            sell_price = prices[s]

            for b in range(s):# valid buy days = [day 0, sell day)
                # [0, 0]
                buy_price = prices[b]
                print(buy_price)
                if sell_price - buy_price > result:
                    result = sell_price - buy_price
        return result