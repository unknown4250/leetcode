class Solution(object):
    def numSpecial(self, mat):
        one_rows, one_cols = [0] * len(mat), [0] * len(mat[0])

        # 각 행, 열에 1이 몇 개씩 있는지 카운팅
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                one_rows[i] += mat[i][j]
                one_cols[j] += mat[i][j]

        count = 0
        
        # 값이 1이면서 그 위치를 포함하는 행, 열에 1이 하나인 경우 탐색
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if one_rows[i] == 1 and one_cols[j] == 1:
                        count += 1
        return count