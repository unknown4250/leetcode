class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x < 2:
            return x

        # binary search를 위한 left, right 포인터
        # x의 제곱근은 무조건 x/2보다 작으므로 right는 x를 2로 나눈 정수부터 시작
        left, right = 1, x // 2

        while left <= right:
            mid = left + (right - left) // 2

            # mid의 제곱이 x보다 크면 right를 왼쪽으로 이동
            if mid * mid > x:
                right = mid - 1
            # mid의 제곱이 x보다 작으면 left를 오른쪽으로 이동
            elif mid * mid < x:
                left = mid + 1
            # mid의 제곱이 x라면, mid 리턴
            else:
                return mid

        # 제곱근이 없을 경우, right를 리턴
        return right
