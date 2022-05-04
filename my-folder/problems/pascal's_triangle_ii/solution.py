class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        # dynamic programming
        answer = [0] * (rowIndex + 1)

        for i in range(len(answer)):
            answer[i] = [0] * (i + 1)
        answer[0] = [1]

        for i in range(rowIndex + 1):
            for j in range(i + 1):
                if j == 0 or j == i:
                    answer[i][j] = 1
                else:
                    answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
        return answer[rowIndex]