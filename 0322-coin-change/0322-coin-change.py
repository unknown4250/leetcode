class Solution(object):
    def coinChange(self, coins, amount):
        """
        # DP Version
        # 코인 개수 저장할 배열 : amount+1로 값 초기화
        dp = [amount+1] * (amount+1)

        dp[0] = 0

        # i: 코인에 의해 만들어지는 값
        for i in range(1, amount+1):
            for coin in coins:
                # 값이 코인보다 큰 경우
                if i >= coin:
                    # 기존 코인 개수와 현재 코인을 더했을 때의 코인 개수 비교
                    dp[i] = min(dp[i], dp[i-coin]+1)

        # amount를 만들지 못하는 경우(=초기화한 값이 그대로인 경우)
        if dp[amount] == amount + 1:
            # -1 리턴
            return -1
        
        return dp[amount]
        """
        # BFS version
        if amount == 0:
            return 0

        queue = deque([(0,0)])

        visited = [True] + [False] * amount

        while queue:
            # 코인 개수, 값
            total_coins, cur_val = queue.popleft()
            total_coins += 1

            # 가지고 있는 코인으로 만들 수 있는 값 조합 탐색
            for coin in coins:
                next_val = cur_val + coin

                # amount와 같다면 현재 코인 개수 리턴
                if next_val == amount:
                    return total_coins

                # amount보다 작으면 이후에 coin 더해서 다시 탐색해야 함
                elif next_val < amount:
                    # 만들어지지 않은 값에 대해서만 탐색
                    if not visited[next_val]:
                        visited[next_val] = True # 해당 값을 만들었다고 표시
                        queue.append((total_coins, next_val))
        
        return -1