class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        
        flatten_mat = sum(mat, [])

        if len(flatten_mat) != r * c:
            return mat
        
        idx = 0
        res = []

        for _ in range(r):
            temp = []
            for _ in range(c):
                temp.append(flatten_mat[idx])
                idx += 1
            res.extend([temp])

        return res