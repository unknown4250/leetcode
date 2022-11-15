class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for t in tokens:
            # 숫자인 경우
            if t not in "+-/*":
                # 스택에 추가
                stack.append(int(t))
            # 연산자인 경우
            else:
                # 오른쪽 숫자, 왼쪽 숫자
                r, l = stack.pop(), stack.pop()
                
                # 덧셈
                if t == "+":
                    stack.append(l + r)
                # 뺄셈
                elif t == "-":
                    stack.append(l - r)
                # 곱셈
                elif t == "*":
                    stack.append(l * r)
                # 나눗셈(결과 truncate해야 함)
                else:
                    stack.append(int(float(l) / r))

        return stack.pop()
        