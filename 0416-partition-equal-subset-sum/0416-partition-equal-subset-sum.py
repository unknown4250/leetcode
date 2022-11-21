class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)

        # 배열의 합이 홀수이면 합이 같은 두 부분 배열로 나눌 수 없음
        if total % 2 == 1:
            return False

        # 배열 전체 합의 절반을 dp 배열의 길이로 설정
        total //= 2

        # dp[i]: i를 만들 수 있는지 여부
        dp = [False] * (total + 1)

        # 초기값 설정
        dp[0] = True

        for num in nums:
            # num 이후의 숫자 중에서 합이 total이 되는 경우 탐색
            for i in range(total, num-1, -1):
                # i를 만들 수 있거나 i-num을 만들 수 있으면 True
                dp[i] = dp[i] or dp[i-num]
        return dp[-1]
        
        
        