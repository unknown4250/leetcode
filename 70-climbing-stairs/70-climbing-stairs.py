class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        result = [0] * (n + 1)
        result[1] = 1
        result[2] = 2
        
        for i in range(3, n + 1):
            result[i] = result[i-1] + result[i-2]
            
        return result[n]