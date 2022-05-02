class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        total = 0

        for i in range(len(digits)):
            total += (10 ** (len(digits) -1 - i)) * digits[i]

        return [i for i in str(total+1)]