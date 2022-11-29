class Solution(object):
    def uniquePaths(self, m, n):

        # 예외 처리
        if m == 0 or n == 0:
            return 0

        # 그리드 초기화
        dp = [[1] * n for _ in range(m)]

        # (0,0), (0,1), (1,0)까지의 unique path는 모두 1가지이므로
        # (1,1)부터 탐색 시작
        for i in range(1, m):
            for j in range(1, n):
                # 왼칸과 윗칸에서 올 수 있는 경로 개수 누적
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]