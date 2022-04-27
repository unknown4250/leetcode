class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        max_num = 0
            
        for i in range(0, len(nums)):
            if nums[i] == 1:
                cnt += 1
                if cnt > max_num:
                    max_num = cnt
            else:
                cnt = 0
            
        return max_num