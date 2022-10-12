class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # any() 활용한 한 줄 풀이
        #return any(target in row for row in matrix)

        if not matrix: return False

        row, col = 0, len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            # 현재 위치보다 타겟 값이 작으면 현재 행의 왼쪽으로 이동
            if target < matrix[row][col]:
                col -= 1
            # 현재 위치보다 타겟 값이 크면 아래 행으로 이동
            elif target > matrix[row][col]:
                row += 1
            else:
                return True

        return False