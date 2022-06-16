class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        
        return len(set(candyType)) if len(candyType)/2 > len(set(candyType)) else len(candyType) // 2