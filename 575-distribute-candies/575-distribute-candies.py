class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        lst_len, set_len = len(candyType), len(set(candyType))
        
        return set_len if lst_len / 2 > set_len else lst_len // 2