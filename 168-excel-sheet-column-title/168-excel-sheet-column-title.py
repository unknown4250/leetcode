class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        res = ''
        
        while columnNumber >= 1:
            tmp = chr((columnNumber - 1) % 26 + 65)
            columnNumber = (columnNumber - 1) // 26
            res = tmp + res
        return res