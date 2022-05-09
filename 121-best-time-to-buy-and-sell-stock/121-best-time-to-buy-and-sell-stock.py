class Solution(object):
    def maxProfit(self, prices):

        """
        # 아래 코드를 dp 관점에서 풀어낸다면 아래와 같다.
        # 코드를 보면 memoization을 위해 배열이 아니라 변수 하나면 된다.
        # dp 배열 -> max_profit으로 변경

        dp = [0] * len(prices)
        min_value = prices[0]

        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i]-min_value)
            min_value = min(min_value, prices[i])
        return result
        """


        max_profit = 0
        min_value = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-min_value)
            min_value = min(min_value, prices[i])
        return max_profit

