class Solution(object):
    def isHappy(self, n):
        # 각 step 마다 제곱의 합을 set에 저장
        # set에 저장하는 이유? set은 값을 검색하는데 O(1)이 걸리는 반면, list는 O(n)이 걸리기 때문
        check = set()

        # 각 자리의 제곱을 더할 변수
        sum_squares = 0  
        while sum_squares != 1:        
            # 입력 값의 자리수마다 제곱을 계산하기 위한 반복문 (for문 -> while로 변경)
            # sum_squares = sum(int(i) ** 2 for i in str(n))
            sum_squares = 0
            while n >= 1:
                sum_squares += (n % 10) ** 2
                n //= 10 
            # "happy"하지 않다면, 그 숫자는 일정 싸이클을 가지고 있어서 제곱 합의 결과 값이 반복됨
            # 그래서 set을 사용해서 중복된 값이 나왔었는지 확인하는 것
            if sum_squares in check: return False
            else:
                n = sum_squares
                check.add(sum_squares)
        return True