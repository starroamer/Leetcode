class Solution(object):
    """
    https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
    """
    from typing import List
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        buy = s1 = sell = s2 = [0 for x in prices]
        s1 = [0 for x in prices]
        sell = [0 for x in prices]
        s2 = [0 for x in prices]
        buy[0] = -prices[0]
        s1[0] = -prices[0]

        for i in range(1, n):
            buy[i] = max(s2[i-1], sell[i-1]) - prices[i]
            s1[i] = max(buy[i-1], s1[i-1])
            sell[i] = max(buy[i-1], s1[i-1]) + prices[i] - fee
            s2[i] = max(s2[i-1], sell[i-1])
            print(i)
            print(buy)
            print(s1)
            print(sell)
            print(s2)

        return max(sell[-1], s2[-1])

if __name__ == "__main__":
    s = Solution()
    prices = [1,3,7,5,10,3]
    fee = 3
    print(s.maxProfit(prices, fee))
