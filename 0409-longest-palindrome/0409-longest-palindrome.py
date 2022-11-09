class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        answer = 0
        odd_check = False # 개수가 홀수인 문자가 있는지 확인

        for count in Counter(s).values():
            # 문자 개수가 짝수이면 팰린드롬 포함 가능
            if count % 2 == 0:
                # 결과에 개수 추가
                answer += count
            else:
                odd_check = True # 문자가 홀수 개 있는 경우
                answer += count - 1  # 해당 문자 중 1개를 제외하면(=짝수) 팰린드롬에 포함 가능 

        # 홀수 개의 문자가 있는 경우엔 가운데 포함시키면 되므로 문자열 길이 + 1
        # 홀수 개의 문자가 없으면, 문자열 길이 그대로
        return answer + 1 if odd_check else answer
