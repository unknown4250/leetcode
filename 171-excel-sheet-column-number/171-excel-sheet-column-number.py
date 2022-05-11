class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """      

        sum = 0
        for i in range(len(columnTitle)):
            sum += (ord(columnTitle[i]) - 64) * (26 ** (len(columnTitle)-i-1))
        return sum