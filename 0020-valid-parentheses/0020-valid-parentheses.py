class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {')':'(', ']':'[', '}':'{'}


        stack = []

        for ch in s:
            # 괄호의 첫 번째 문자인 경우
            if ch not in parentheses:
                # 스택에 삽입
                stack.append(ch)

            # 스택이 비었거나, 스택 마지막 값이 현재 괄호와 짝이 아닌 경우
            elif not stack or parentheses[ch] != stack.pop():
                # False 리턴
                return False

        # 스택에 문자가 남아있는 경우 False, 스택이 비어있으면 True 리턴
        return not stack