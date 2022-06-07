class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        
        n = len(prices)
        dp = [0] * n
        max_profit = dp[0] - prices[0] - fee

        for i in range(1, n):
            dp[i] = max(dp[i-1], prices[i] + max_profit)
            max_profit = max(max_profit, dp[i] - prices[i] - fee)
        return dp[n-1]