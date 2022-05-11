class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for n in nums:
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
            
            if dict[n] > len(nums) / 2:
                return n