class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return list(set([i for i in range(len(nums) + 1)]) - set(nums))[0]