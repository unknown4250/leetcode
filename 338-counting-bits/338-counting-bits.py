class Solution(object):
    def countBits(self, n):
        """
        # 패턴 찾아내기
        # i가 2의 n제곱이 될 때마다 offset 값 변경해야 함 
        dp[0] = 0
        dp[1] = dp[0] + 1 = dp[1-1] + 1
        dp[2] = dp[0] + 1 = dp[2-2] + 1
        dp[3] = dp[1] + 1 = dp[3-2] + 1
        dp[4] = dp[0] + 1 = dp[4-4] + 1
        dp[5] = dp[1] + 1 = dp[5-4] + 1
        dp[6] = dp[2] + 1 = dp[6-4] + 1
        dp[7] = dp[3] + 1 = dp[7-4] + 1
        dp[8] = dp[0] + 1 = dp[8-8] + 1
        """
        offset = 1
        result = [0] * (n+1)
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset *= 2
            result[i] = result[i-offset] + 1
        return result