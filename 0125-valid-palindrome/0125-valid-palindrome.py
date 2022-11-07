class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 문자열의 양 끝을 가리키는 포인터
        l, r = 0, len(s) - 1

        while l <= r:
            # 문자열이 문자나 숫자가 아니면 왼쪽 포인터 오른쪽으로 이동
            if not s[l].isalnum():
                l += 1
    
            # 문자열이 문자나 숫자가 아니면 오른쪽 포인터 왼쪽으로 이동
            elif not s[r].isalnum():
                r -= 1
            
            # 양쪽 문자가 같지 않으면 False 리턴
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    # 양쪽 포인터 이동
                    l += 1
                    r -= 1

        return True