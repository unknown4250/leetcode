class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # with DP
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
    
        """
        # with Two Pointers        
        # 현재 값보다 다음 값이 크면 profit 생기는 것
        # left는 현재 값
        # 배열 값이 증가할 때까지 right 증가시키기
        # prices[right] - prices[left] = 하나의 profit
        # left는 right로 옮겨감
        left, right = 0, 1
        profit = 0
        while left < len(prices):
            while right < len(prices):
                if prices[left] <= prices[right]:
                    profit += (prices[right] - prices[left])
                    right += 1
                    left += 1
                else:
                    break
            left = right
            right = left + 1
        return profit
        """