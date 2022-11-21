class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        # dp[i]는 s[:i]까지 wordDict에 있는 단어로 만들 수 있는지 여부
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            # 현재 위치까지의 문자열을 만들 수 있다면
            if dp[i]:
                # 이후의 문자열을 만들 수 있는지 탐색
                for j in range(i+1, len(s)+1):
                    # 길이를 늘려가며 단어가 있는지 확인
                    if s[i:j] in wordDict:
                        # 해당 위치까지는 문자열을 만들 수 있음을 표시
                        dp[j] = True
        return dp[-1]