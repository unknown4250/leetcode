class Solution(object):
    def tribonacci(self, n):
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        
        d = [0] * (n+1)
        d[0], d[1], d[2] = 0, 1, 1

        for i in range(3, n + 1):
            d[i] = d[i-3] + d[i-2] + d[i-1]
            
        return d[n]

