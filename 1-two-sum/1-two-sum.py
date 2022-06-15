class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        temp_dict = {}

        for i, n in enumerate(nums):
            if n in temp_dict:
                return [temp_dict[n], i]
            else:
                temp_dict[target-n] = i