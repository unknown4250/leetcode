class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        # 시작점에 방해물 있는 경우 이동 불가
        if obstacleGrid[0][0]:
            return 0

        # grid의 세로, 가로 길이
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # grid의 위치마다 이동 방법 수 저장할 배열
        dp = [[0] * n for _ in range(m)]

        # 시작점
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                # 시작점이거나 장애물 놓여있을 때 경우의 수 계산 안함
                if (i == 0 and j == 0) or obstacleGrid[i][j]:
                    continue

                # space일 경우
                if not obstacleGrid[i][j]:
                    # grid의 top이나 left는 각각 왼쪽, 위쪽으로부터만 경우의 수 계산 가능하므로 예외 처리
                    dp[i][j] = (dp[i-1][j] if i else 0) + (dp[i][j-1] if j else 0)

        return dp[-1][-1]