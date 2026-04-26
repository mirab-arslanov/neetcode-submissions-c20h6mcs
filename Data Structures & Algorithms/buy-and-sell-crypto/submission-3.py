class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1, 0, -1):
            buy = min(prices[0:i])
            if buy >= prices[i]:
                continue
            res = max(res, prices[i] - buy)
        return res
            