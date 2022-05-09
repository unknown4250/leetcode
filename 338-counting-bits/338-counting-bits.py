class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        offset = 1
        result = [0] * (n+1)
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset *= 2
            result[i] = result[i-offset] + 1
        return result