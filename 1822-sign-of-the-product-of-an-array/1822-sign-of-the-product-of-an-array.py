class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        ans = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                ans *= -1
        
        return ans