class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        best_profit = 0
        while buy < len(prices) - 1:
            sell = buy + 1
            while sell < len(prices):
                if prices[buy] < prices[sell]:
                    curr_profit = prices[sell] - prices[buy]
                    best_profit = max(best_profit, curr_profit)
                sell += 1
            buy += 1
        return best_profit
            