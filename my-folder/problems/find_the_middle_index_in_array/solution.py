class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        right_sum = 0
        
        for i in range(len(nums)):
            right_sum += nums[i]
            
        for i in range(len(nums)):
            right_sum -= nums[i]
            
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
        return -1
        