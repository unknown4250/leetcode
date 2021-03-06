class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        if N == 1: return

        for i in range(N//2):
            for j in range(N):
                matrix[i][j], matrix[N-i-1][j] = matrix[N-i-1][j], matrix[i][j]

        for i in range(N):
            for j in range(N):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]