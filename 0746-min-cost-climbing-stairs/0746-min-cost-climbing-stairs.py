class Solution(object):
    def minCostClimbingStairs(self, cost):
        # dp 배열 초기화
        dp = [0] * len(cost)
        
        # 예외처리
        if not cost:
            return 0
        
        elif len(cost) == 1:
            return cost[0]

        # 인덱스 0, 1번째 값으로 초기화
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            # 현재 위치까지의 최소 비용 : 현재 비용 + 1스텝 전 or 2스텝 전 중 최솟값
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])