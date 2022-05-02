class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        result = []
        i = j = 0
        
        while i < len(mat) and j < len(mat[0]):
            # left_to_right
            while i >= 0 and j < len(mat[0]):
                result.append(mat[i][j])
                if j == len(mat[0]) - 1:
                    i += 1
                    break 
                elif i == 0:
                    j += 1
                    break
                else:
                    i -= 1
                    j += 1
            # right_to_left
            while j >= 0 and i < len(mat):
                result.append(mat[i][j])
                if i == len(mat) - 1:
                    j += 1
                    break
                elif j == 0:
                    i += 1
                    break
                else:
                    i += 1
                    j -= 1
                
        return result
        