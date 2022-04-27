class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for num in nums:
            digit = 1
            
            while True:
                if num / 10 >= 1:
                    digit += 1
                    num /= 10
                else:
                    break
            if digit % 2 == 0:
               cnt += 1
        return cnt
        