class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        
        return (high - low) // 2 + (low % 2 or high % 2)