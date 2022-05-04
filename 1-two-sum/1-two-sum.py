class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """    
        # Brute force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[j] == nums[i]:
                    return [i, j]
