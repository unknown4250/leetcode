class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        # with extra space
        temp = []
        result = []

        N = len(matrix)
        for i in range(N):
            temp = []
            for j in range(N):
                temp.append(matrix[N-1-i][j])
            result.append(temp)
        print(result)
        """

        # in-place로 풀어야함
        # element 하나하나에 접근하면서 1:1로 값을 바꾸게 되면
        # 초기 matrix 값이 바뀌어서 원하는 답 못 찾게 됨 
        # input을 어떻게 바꿔야 output이 될지 생각해야 함
        # 1. 행을 기준으로 뒤집는다
        # 2. 대각선을 기준으로 뒤집는다
        # 여기서 대각선은 i와 j 값이 같은 element를 의미한다 
        N = len(matrix)
        if N == 1: return

        for i in range(N//2):
            for j in range(N):
                matrix[i][j], matrix[N-i-1][j] = matrix[N-i-1][j], matrix[i][j]

        for i in range(N):
            for j in range(N):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]