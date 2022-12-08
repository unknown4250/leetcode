class Solution(object):
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1

        result = []

        while top <= bottom and left <= right:
            # top left to top right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # top right to bottom right
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # bottom right to bottom left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

            # bottom left to top left
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

        return result[:m*n]