class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            result = int(str(x)[::-1])
        else:
            result = int(str(x*-1)[::-1]) * -1
        
        if result >= 2**31 or result <= -2**31:
            return 0
        else:
            return result