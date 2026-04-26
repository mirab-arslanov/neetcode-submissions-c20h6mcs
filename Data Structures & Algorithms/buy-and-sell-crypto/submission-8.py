class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy, sell = 0, 1
        leng = len(prices)
        while sell < leng and buy < leng:
            if prices[sell] <= prices[buy]:
                buy += 1
                while sell == buy:
                    sell += 1
            else:
                res = max(res, prices[sell] - prices[buy])
                sell += 1
        return res
            