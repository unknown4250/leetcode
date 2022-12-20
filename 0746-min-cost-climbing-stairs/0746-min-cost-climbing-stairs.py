class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        # [10,15,20] = (시작) → 10 → 15 → 20 → (종료)
        # 한 번에 1개 혹은 2개의 계단을 오를 수 있음
        # 가능한 경우의 수 : (10, 15, 20), (10, 15), (10, 20), (15, 20), (15)
        """
        min_cost = [0] * len(cost)
        min_cost[0], min_cost[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            min_cost[i] = min(min_cost[i-2] + cost[i], min_cost[i-1] + cost[i])

        return min(min_cost[len(cost) - 1], min_cost[len(cost) - 2])