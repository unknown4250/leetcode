class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        """
        sum, j = 0, 0
        mat_len, arr_len = len(mat), len(mat[0])

        if mat_len % 2 == 1 or mat_len == 0:
            mat_len = int(len(mat)/2) + 1
        else:
            mat_len = int(len(mat)/2)

        for i in range(mat_len):
            if i == arr_len-1-j:
                sum += mat[i][j]
            else:
                sum += (mat[i][j] + mat[i][arr_len-1-j] + mat[len(mat) -1 -i][j] + mat[len(mat) -1 -i][arr_len-1-j])
            j += 1
        return sum
        """
        res = 0
        n = len(mat)
        for i in range(len(mat)):
            res += mat[i][i]
            res += mat[n-1-i][i]
        
        if n % 2 == 1:
            res -= mat[n//2][n//2]

        return res