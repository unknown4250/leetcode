class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        dict = {}
        for i, num in enumerate(numbers):
            if target - num in dict:
                return [dict[target-num], i + 1]
            else:
                dict[num] = i + 1